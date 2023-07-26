#Cryptography Challenge #1 - www.101computing.net/cryptography-challenge-1/

import random, time

def encrypt(plaintext, key):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+"
    ciphertext = ""
    for i in range(0, len(plaintext)):
        character = plaintext[i]
        ciphertext = ciphertext + character
        for j in range(0, key):
            ciphertext = ciphertext + random.choice(chars)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in range(0, len(ciphertext), key+1):
        plaintext += ciphertext[char]
    return plaintext

plaintext = input("Enter a message to encrypt (plaintext):\n")
key = int(input("Input a key as a number between 1 and 10:\n"))
while not (key >= 1 and key <= 10):
    print("Invalid key, try again!")
    key = int(input("Input a key as a number between 1 and 10"))

time.sleep(1)
print("\nEncrypting plaintext...")
time.sleep(1)
print("...")
time.sleep(1)
ciphertext = encrypt(plaintext, key)

print("Ciphertext:")
print(ciphertext)

time.sleep(3)

time.sleep(1)
print("\nDecrypting ciphertext...")
time.sleep(1)
print("...")
time.sleep(1)
plaintext = decrypt(ciphertext, key)

print("Original plaintext:")
print(plaintext)

#print(decrypt("PHcRrveeRUmDnfqMFAnBJvvwyzSDrj tqXhrLRXIegaDLwdInIGCvqelcjzU", 5))