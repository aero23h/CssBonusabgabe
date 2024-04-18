
# Das CSS Team wuenscht Ihnen einen
# guten Rutsch ins neue Jahr! Wir freuen uns Sie in 2024 wieder zu sehen.


def xor_operation(key, message):
    key_ascii = [ord(char) for char in key]
    text_ascii = [ord(char) for char in message]
    result = []

    for i in range(len(text_ascii)):
        result.append(text_ascii[i] ^ key_ascii[i % len(key_ascii)])

    return ''.join([chr(num) for num in result])


def electronic_code_book(key, message):
    encrypted_string = ""

    for i in range(0, len(message), 7):
        block = message[i:i + 7]
        encrypted_string += xor_operation(block, str(key))

    return encrypted_string


def string_to_hex(input_string):
    return ' '.join(format(ord(char), '02x') for char in input_string)


def main():

    key = 1234567
    message = "Das CSS Team wuenscht Ihnen einen guten Rutsch ins neue Jahr! Wir freuen uns Sie in 2024 wieder zu sehen."

    chiffrat = electronic_code_book(key, message)
    print("Chiffrat:\n" + string_to_hex(chiffrat) + "\n")

    decryption = electronic_code_book(key, chiffrat)
    print("Entschlüsseltes Chiffrat:\n" + decryption)


if __name__ == '__main__':
    main()


