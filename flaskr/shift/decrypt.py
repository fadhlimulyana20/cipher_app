def decrypt(cipher_text: str, s: int) -> str:
    plain_text = ""

    for c in cipher_text:
        # Check if character is an uppercase letter
        if c.isupper():
            # Find position of alphabet
            c_index = ord(c) - ord("A")

            # Perform negative shift
            new_index = (c_index - s) % 26

            # Convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # Append new character to plain text
            plain_text += new_character

        elif c.islower():
            # Calculate the index
            c_index = ord(c) - ord("a")

            # Perform the shift
            new_index = (c_index - s) % 26

            # Convert new index to character
            new_unicode = new_index + ord("a")

            new_character = chr(new_unicode)

            plain_text += new_character

        else:
            # Leave it as it is
            plain_text += c

    return plain_text


if __name__ == "__main__":
    cipher_text = "KHOOR ZRUOG"
    s = 3
    plain_text = decrypt(cipher_text, s)
    print(plain_text)
