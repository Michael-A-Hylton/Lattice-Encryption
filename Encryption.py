import numpy as np
import secrets

def createPublicKey(size, max_value=256):

    return ([secrets.randbelow(max_value) for _ in range(size)])

#def selectKey(numbersList, listSize):
 #   indices = secrets.SystemRandom().sample(range(len(numbersList)), listSize)
  #  subset = [numbersList[i] for i in indices]
   # return subset, indices

def file2binary(filePath):
    with open(filePath, "rb") as file:
        content = file.read()
    return np.unpackbits(np.frombuffer(content, dtype=np.uint8))


def encryptBinaryData(binaryData, publicKey):
    cipherText = []
    for bit, num in zip(binaryData, publicKey):
        if bit:
            cipherText.append(num)  # Ensure the number is in the byte range (0-255)
        else:
            cipherText.append(0)  # For bit = 0, append 0
    return cipherText

def main():
    listSize = 1000
    maxVal=256

    publicKey=createPublicKey(listSize, maxVal)
    print("Provide the filepath of file to encrypt: ")
    file2encrypt=input()
    #file2encrypt=file2encrypt[6:]
    newfile="encyrptedFile.bin"
    keyfile="encryptionKey.txt"


    binaryData=file2binary(file2encrypt)
    binaryLength = len(binaryData)
    # if there is more bits then our array size, we split it
    chunks=np.array_split(binaryData,-(-binaryLength //listSize))


    ciphertexts = [encryptBinaryData(chunk, publicKey)for chunk in chunks]

    with open(newfile, "wb") as file:  # Open file in binary write mode
        for chunk in ciphertexts:
            for num in chunk:
                file.write(bytes([num]))  # Write each byte
    print(f"Encrypted file saved as {newfile}")

    with open(keyfile, "w") as file:
        file.write(f"{listSize}\n{binaryLength}\n")
        file.writelines(f"{num}\n"for num in publicKey)
    print(f"Encryption key saved as {keyfile}")

if __name__ == "__main__":
    main()