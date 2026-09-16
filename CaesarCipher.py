def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0

    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt += 1

    return key


# Encryption
def encrypt(key, message):
    cipher = ""

    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c

    return cipher


# Decryption
def get_decryption_key(key):
    dkey = {}

    for c in key:
        dkey[key[c]] = c

    return dkey


key = generate_key(3)
print(key)

message = "DAMINDA HERATH"

cipher = encrypt(key, message)
print(cipher)

dkey = get_decryption_key(key)

message = encrypt(dkey, cipher)
print(message)
