# Das CSS Team wuenscht Ihnen einen
# guten Rutsch ins neue Jahr! Wir freuen uns Sie in 2024 wieder zu sehen.


def xor_operation(key, message):
    key_ascii = [ord(char) for char in key]
    text_ascii = [ord(char) for char in message]

    result = []
    for i in range(len(text_ascii)):
        result.append(chr(text_ascii[i] ^ key_ascii[i]))

    return ''.join(result)


def ctr_encrypt(key, message):
    encrypted_string = ""
    counter = 1
    adjusted_key = str(key)

    for i in range(0, len(message), 7):
        block = message[i:i + 7]
        counter_bytes = counter.to_bytes(7, byteorder='big')
        encrypted_block = xor_operation(adjusted_key, counter_bytes.decode())
        encrypted_string += xor_operation(encrypted_block, block)

        counter += 1

    return encrypted_string


def ctr_decrypt(key, chiffre):
    decrypted_string = ""
    counter = 1
    adjusted_key = str(key)[:7]

    for i in range(0, len(chiffre), 7):
        block = chiffre[i:i + 7]
        counter_bytes = counter.to_bytes(7, byteorder='big')
        decrypted_block = xor_operation(adjusted_key, counter_bytes.decode())
        decrypted_string += xor_operation(decrypted_block, block)

        counter += 1

    return decrypted_string


def string_to_hex(input_string):
    return ' '.join(format(ord(char), '02x') for char in input_string)


def main():
    key = 1234567
    message = "Das CSS Team wuenscht Ihnen einen guten Rutsch ins neue Jahr! Wir freuen uns Sie in 2024 wieder zu sehen."

    chiffrat = ctr_encrypt(key, message)
    print("Chiffrat:\n" + string_to_hex(chiffrat) + "\n")

    decryption = ctr_decrypt(key, chiffrat)
    print("Entschlüsseltes Chiffrat:\n" + decryption)


if __name__ == '__main__':
    main()
