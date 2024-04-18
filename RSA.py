from sympy import mod_inverse


def gen_d():
    e = 65537
    phi_n = 170158346318205037787035915821869858640  # berechnetes φ(N)

    return mod_inverse(e, phi_n)


def encrypt_rsa(d, message):
    N = 170158346318205037813391079914939294003

    return pow(message, d, N)


def decrypt_rsa(message):
    e = 65537
    N = 170158346318205037813391079914939294003

    return pow(message, e, N)


if __name__ == '__main__':

    message = 2521215

    d = gen_d()
    result = encrypt_rsa(d, message)
    print("Verschlüseselt: " + str(result))

    decryption = decrypt_rsa(result)
    print("Entschlüsselt: " + str(decryption))