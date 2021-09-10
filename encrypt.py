def encrypt(text: str, s: int) -> str:
    encryption: str = ""

    for c in text:
        # check if character is uppercase letter
        if c.isupper():
            # # find the position of the caharacter in ANSI code
            # c_unicode = ord(c)

            # Calculate the index
            c_index = ord(c) - ord("A")

            # Perform the shift
            new_index = (c_index + s) % 26

            # Convert new index to character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            encryption += new_character

        elif c.islower():
            # Calculate the index
            c_index = ord(c) - ord("a")

            # Perform the shift
            new_index = (c_index + s) % 26

            # Convert new index to character
            new_unicode = new_index + ord("a")

            new_character = chr(new_unicode)

            encryption += new_character

        else:
            # Since character is neither uppercase nor lowercase, leave it as it is
            encryption += c

    return encryption


if __name__ == "__main__":
    plaintext = "HELLO WORLD"
    s = 3
    ciphertext = encrypt(plaintext, 3)
    print(ciphertext)
