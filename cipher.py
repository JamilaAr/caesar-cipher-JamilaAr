def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            # Non-alphabetical characters remain the same
            encrypted_text += char
            return encrypted_text

def main():
    sentence = input("Please enter a sentence: ")
    shift = 5
    encrypted_sentence = caesar_cipher(sentence, shift)
    print("The encrypted sentence is:", encrypted_sentence)

if __name__ == "__main__":
    main()
