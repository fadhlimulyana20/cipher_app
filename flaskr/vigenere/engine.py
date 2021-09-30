def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return "".join(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(text, key):
    cipher_text = []
    for i in range(len(text)):
        if (ord(text[i]) == 32):
            cipher_text.append(" ")
            continue

        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def decrypt(text, key):
    cipher_text = []
    for i in range(len(text)):
        if (ord(text[i]) == 32):
            cipher_text.append(" ")
            continue

        x = (ord(text[i]) - ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)
