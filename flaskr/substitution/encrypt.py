import string


def encrypt(plain_text: str, key: int):
    all_letters = string.ascii_letters

    dict1 = {}

    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i+key) % len(all_letters)]

    cipher_text = []

    for char in plain_text:
        if char in all_letters:
            temp = dict1[char]
            cipher_text.append(temp)
        else:
            temp = char
            cipher_text.append(temp)

    cipher_text = "".join(cipher_text)

    return cipher_text

if __name__ == "__main__":
    plain_txt= "I am studying Data Encryption"
    key = 4
    print(encrypt(plain_txt, key))

    