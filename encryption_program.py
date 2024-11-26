import numpy as np
import secrets
import os
import struct

def createPublicKey(size, max_value=4294967):
    return [secrets.randbelow(max_value) for _ in range(size)]

def selectRandomSubset(numbersList, subset_size):
    # Select random 500 numbers from the 1000
    indices = secrets.SystemRandom().sample(range(len(numbersList)), subset_size)
    subset = [numbersList[i] for i in indices]
    return subset, indices

def file2binary(filePath):
    with open(filePath, "rb") as file:
        content = file.read()
    binary = np.unpackbits(np.frombuffer(content, dtype=np.uint8))
    return binary, len(content)

def encryptBinaryData(binaryData, publicKeySubset):
    cipherText = []
    for bit, num in zip(binaryData, publicKeySubset):
        if bit:
            cipherText.append(num)  # For bit = 1, append number from public key
        else:
            cipherText.append(0)  # For bit = 0, append 0
    return cipherText

def main():
    listSize = 1000
    subsetSize = 500  # We are going to use a subset of 500
    maxVal = 4294967

    publicKey = createPublicKey(listSize, maxVal)
    print("Provide the filepath of the file to encrypt: ")
    file2encrypt = input()  # Path of file to encrypt
    newfile = "encryptedFile.bin"  # Output encrypted file
    keyfile = "encryptionKey.txt"  # Output key file
    publicKeyFile = "publicKey.txt"

    # Select a random subset of 500 numbers
    publicKeySubset, selected_indices = selectRandomSubset(publicKey, subsetSize)

    binaryData, ogFileLength = file2binary(file2encrypt)  # Get binary data and original file length
    binaryLength = len(binaryData)

    # Split the binary data into chunks for encryption
    chunks = np.array_split(binaryData, -(-binaryLength // listSize))

    # Encrypt each chunk
    ciphertexts = [encryptBinaryData(chunk, publicKeySubset[:len(chunk)]) for chunk in chunks]

    with open(newfile, "wb") as file:  # Open file in binary write mode
        for chunk in ciphertexts:
            for num in chunk:
                packed=struct.pack('>I',num)
                file.write(packed)  # Write encrypted data as bytes
    print(f"Encrypted file saved as {newfile}")

    # Save the encryption key
    with open(keyfile, "w") as file:
        file.write(f"{listSize}\n{binaryLength}\n")
        file.write(f"{ogFileLength}\n")
        file.write(f"{subsetSize}\n")  # Store the subset size
        file.writelines(f"{num}\n" for num in publicKeySubset)
    print(f"Encryption key saved as {keyfile}")

    #save the public key
    with open(publicKeyFile, "w") as file:
        file.writelines(f"{num}\n" for num in publicKey)
    print(f"Public key saved as {publicKeyFile}")

if __name__ == "__main__":
    main()
