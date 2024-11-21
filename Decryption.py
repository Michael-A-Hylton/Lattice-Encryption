import numpy as np

def binary2file(binary, outputPath):
    byteData = np.packbits(binary).tobytes()
    with open(outputPath, "wb") as file:
        file.write(byteData)

def decryptText(ciphertext, numbers_list, binary_length):
    binary_data = []
    for num in numbers_list:  # Process each number in the numbers_list
        if ciphertext >= num:
            binary_data.append(1)
            ciphertext -= num
        else:
            binary_data.append(0)
    return np.array(binary_data[:binary_length], dtype=np.uint8)

def main():
    # File paths
    print("Input the filepath of the encrypted file: ")
    encryptedFile = input() #Should be encrypted.bin
    keyFile = "encryptionKey.txt"
    decryptedFile = "decryptedFile.txt"

    # Load encryption key
    with open(keyFile, "r") as file:
        lines = file.readlines()
    list_size = int(lines[0].strip())
    binary_length=int(lines[1].strip())
    numbers_list = list(map(int, lines[2:]))


    # Load ciphertexts
    with open(encryptedFile, "rb") as file:
        ciphertext = file.read()

    ciphertexts = list(ciphertext)

    # Decrypt each chunk
    decryptedChunks = []
    for byte in ciphertexts:
        chunk_length = min(list_size, binary_length)  # Each chunk uses the full list size
        decryptedChunks.append(decryptText(byte, numbers_list, chunk_length))  # Pass byte as single value
        binary_length -= chunk_length
    # Reconstruct binary data from chunks
    decrypted_binary = np.concatenate(decryptedChunks)

    # Convert binary back to file
    binary2file(decrypted_binary, decryptedFile)
    print(f"Decrypted file saved as {decryptedFile}")

if __name__ == "__main__":
    main()
