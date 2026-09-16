from pyDes import *
message = "0123456701234567"
key = "DESCRYPT"
iv = bytes([0]*8)


# create the cipher here
k=des(key,CBC,iv,pad=None, padmode=PAD_PKCS5)

# Alice sending the encrypted message
cipher=k.encrypt(message)

# encrypt the message to cipher
print("Length of plain text:", len(message))
print("Length of ciphertext:", len(cipher))
print("Encrypted:", cipher)

message=k.decrypt(cipher)
print("Decrypted:", message)
