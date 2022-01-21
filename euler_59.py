# Project Euler Problem 59
# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

from collections import Counter
import sys

def CheckEnglish(a1, a2):
    xor = a1 ^ a2
    if 32 <= xor <= 90:
        return True
    elif 97 <= xor <= 122:
        return True
    return False

def TryString(a, l):
    c = []
    for i in l:
        c.append(chr(a ^ i))
    if Counter(c).most_common(1)[0][0] == 'e':
        return True
    return False

f = open("p059_cipher.txt", "r")
content = f.read()
content_list = [int(i) for i in content.strip().split(',')]
f.close()

c1 = []
c2 = []
c3 = []

for i in range(0, len(content_list), 3):
    c1.append(content_list[i])
    c2.append(content_list[i + 1])
    c3.append(content_list[i + 2])

password = chr(Counter(c1).most_common(1)[0][0] ^ ord(' ')) + chr(Counter(c2).most_common(1)[0][0] ^ ord(' ')) + chr(Counter(c3).most_common(1)[0][0] ^ ord(' '))                   # Assuming spaces will be the most common character, extract the password through reverse xor

print("Password: ", password)

decrypted = ''

for i in range(len(c1)):
    decrypted = decrypted + chr(c1[i] ^ ord(password[0])) + chr(c2[i] ^ ord(password[1])) + chr(c3[i] ^ ord(password[2]))   # Cycle through password characters and encrypted message

print("Decrypted text:\n\n\"", decrypted, "\"")

answer = 0

for i in decrypted:
    answer = answer + ord(i)

print("\nSum of all ascii values of letters in plain text:", answer)
