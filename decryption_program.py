import numpy as np
import os

def binary2file(binary, outputPath, ogFileLength):
    byteData = np.packbits(binary)[:ogFileLength].tobytes()  # Convert binary to byte data
    with open(outputPath, "wb") as file:
        file.write(byteData)  # Write the byte data back to file

def decryptData(ciphertext_chunk, publicKeySubset):
    binary_data = []
    for cipher, num in zip(ciphertext_chunk, publicKeySubset):  # Process each number in the ciphertext
        if cipher == num:
            binary_data.append(1)  # If numbers match, it's a bit 1
        else:
            binary_data.append(0)  # If numbers don't match, it's a bit 0
    return np.array(binary_data, dtype=np.uint8)

def main():
    print("Input the filepath of the encrypted file: ")
    encryptedFile = input()  # Path of encrypted file
    print("Input the filepath for the encryption key: ")
    keyFile = input()  # Key file name
    print("Input the name for the decrypted file: ")
    decryptedFile = input()  # Output decrypted file name

    # Load encryption key
    with open(keyFile, "r") as file:
        lines = file.readlines()
    list_size = int(lines[0].strip())
    binary_length = int(lines[1].strip())
    ogFileLength = int(lines[2].strip())
    #subset_size = int(lines[3].strip())
    publicKeySubset = list(map(int, lines[4:]))

    # Load ciphertext
    with open(encryptedFile, "rb") as file:
        ciphertext = list(file.read())  # Read encrypted file as byte data

    # Split the ciphertext into chunks
    ciphertexts = np.array_split(list(ciphertext), -(-binary_length // list_size))

    # Decrypt each chunk
    decryptedChunks = []
    for ciphertext_chunk in ciphertexts:
        decryptedChunks.append(decryptData(ciphertext_chunk, publicKeySubset[:len(ciphertext_chunk)]))

    # Reconstruct the binary data from the decrypted chunks
    decrypted_binary = np.concatenate(decryptedChunks)[:binary_length]

    # Convert the binary back to file
    binary2file(decrypted_binary, decryptedFile, ogFileLength)
    print(f"Decrypted file saved as {decryptedFile}")

if __name__ == "__main__":
    main()
