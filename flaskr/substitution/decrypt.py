import string

def decrypt(cipher_text: str, key: 4):
    all_letters = string.ascii_letters

    ditc1 = {}

    for i in range(len(all_letters)):
        ditc1[all_letters[i]] = all_letters[(i-key)%len(all_letters)]

    plain_text = []

    for char in cipher_text:
        if char in all_letters:
            temp = ditc1[char]
            plain_text.append(temp)
        else:
            temp = char
            plain_text.append(temp)

    plain_text = "".join(plain_text)
    return plain_text

if __name__ == "__main__":
    cipher_txt= "M eq wxyhCmrk Hexe IrgvCtxmsr"
    key = 4
    print(decrypt(cipher_txt, key))