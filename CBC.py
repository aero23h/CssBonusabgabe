# Das CSS Team wuenscht Ihnen einen
# guten Rutsch ins neue Jahr! Wir freuen uns Sie in 2024 wieder zu sehen.


def xor_operation(key, message):
    key_ascii = [ord(char) for char in key]
    text_ascii = [ord(char) for char in message]

    result = []
    for i in range(len(text_ascii)):
        result.append(text_ascii[i] ^ key_ascii[i % len(key_ascii)])

    return ''.join([chr(num) for num in result])


def string_to_hex(input_string):
    return ' '.join(format(ord(char), '02x') for char in input_string)


def cipher_block_chaining(key, message):
    encrypted_string = ""
    prev = '\x00' * 7

    for i in range(0, len(message), 7):
        block = message[i:i + 7]
        tmp = xor_operation(prev, block)
        encrypted_block = xor_operation(tmp, str(key))
        encrypted_string += encrypted_block
        prev = encrypted_block

    return encrypted_string


def cbc_decrypt(key, chiffre):
    decrypted_string = ""
    prev = '\x00' * 7

    for i in range(0, len(chiffre), 7):
        block = chiffre[i:i + 7]
        tmp = xor_operation(prev, block)
        xored_block = xor_operation(str(key), tmp)
        decrypted_string += xored_block
        prev = block

    return decrypted_string


def main():
    key = 1234567
    message = "Das CSS Team wuenscht Ihnen einen guten Rutsch ins neue Jahr! Wir freuen uns Sie in 2024 wieder zu sehen."

    chiffrat = cipher_block_chaining(key, message)

    print("Chiffrat:\n" + string_to_hex(chiffrat) + "\n")

    decryption = cbc_decrypt(key, chiffrat)
    print("Entschlüsseltes Chiffrat:\n" + decryption)


if __name__ == '__main__':
    main()
