import csv
import hashlib


# Extrahiert das Salt aus einer gehashten Passwortzeile
def extract_salt(file_path_hashes, css_id):
    password = get_hash(file_path_hashes, css_id)
    password_parts = password.split('$')
    salt = password_parts[-1]

    return salt


# Zählt die Anzahl der Zeilen in der Datei
def count_lines_and_process(file_path):
    total_lines = 0
    with open(file_path, mode='r', encoding='utf8') as file:
        for _ in file:
            total_lines += 1
    return total_lines


# Holt den gesamten Hashwert aus der CSV-Datei
def get_hash(file_path_hashes, css_id):
    try:
        with open(file_path_hashes, mode='r', encoding='utf8') as file:
            csv_reader = csv.reader(file)
            for i, row in enumerate(csv_reader):
                if i == css_id and len(row) > 1:
                    return row[1]
    except FileNotFoundError:
        print(f"Datei {file_path_hashes} nicht gefunden.")
    return None


# Extrahiert den Passworthash aus der CSV-Datei
def extract_password_hash(file_path_hashes, css_id):
    with open(file_path_hashes, mode='r', encoding='utf8') as file:
        csv_reader = csv.reader(file)
        password_list = list(csv_reader)

    password = password_list[css_id][1].split('$')[-2]

    return password


# Überprüft, ob zwei Hashes identisch sind
def check_hashes(hash1, hash2):
    print("\nPrüfe auf Gleichheit der Hashes...")

    if hash1 == hash2:
        print("Hashes sind gleich!")
    else:
        print("Hashes nicht gleich!")


def rainbow_attack(file_path_hashes, file_path_passwords, css_id):
    salt = extract_salt(file_path_hashes, css_id)
    password_hash = extract_password_hash(file_path_hashes, css_id)

    with open(file_path_passwords, mode='r', encoding='utf8') as file:
        for line in file:
            line = line.strip()
            if hashlib.sha256((line + salt).encode()).hexdigest() == password_hash:
                print("Gefundenes Passwort: " + line)
                return line  # Rückgabe des gefundenen Passworts

    return None  # Rückgabe von None, falls kein Passwort gefunden wurde


# Führt eine verstärkte Form des Rainbow Table-Angriffs durch mit mehreren Hash-Durchläufen
def hard_rainbow_attack(file_path_hashes, file_path_passwords, css_id):
    salt = extract_salt(file_path_hashes, css_id)
    password_hash = extract_password_hash(file_path_hashes, css_id)
    counter = 0
    total_lines = sum(1 for _ in open(file_path_passwords, 'r', encoding='utf8'))
    update_interval = total_lines // 20

    with open(file_path_passwords, mode='r', encoding='utf8') as file:
        print("\nHard-rainbow-attack...")

        for line in file:
            line = line.strip()
            tmp = (line + salt).encode()
            hasher = hashlib.sha256()
            hasher.update(tmp)
            tmp_hash = hasher.hexdigest()

            for i in range(1, 101):
                if password_hash == tmp_hash:
                    print("Gefundenes Passwort: " + line + " bei " + str(i) + " Durchläufen")
                    return line, i

                hasher = hashlib.sha256()
                hasher.update(tmp_hash.encode())
                tmp_hash = hasher.hexdigest()
                counter += 1

            if counter % update_interval == 0:
                progress = round(counter / total_lines)
                print(f"Fortschritt: {progress}%")

        print("Nichts gefunden")


# Verschlüsselt ein Passwort mehrfach zur Überprüfung
def hard_encrypt(password, iterations, file_path_hashes, css_id):
    hasher = hashlib.sha256()
    hasher.update((password + extract_salt(file_path_hashes, css_id)).encode())
    tmp = hasher.hexdigest()
    print("\nHard-encrypt Hash...")
    for i in range(iterations - 1):
        hasher = hashlib.sha256()
        hasher.update(tmp.encode())
        tmp = hasher.hexdigest()
    print("Password \"" + password + "\" wurde " + str(iterations) + " mal gehasht: " + tmp)
    return tmp


def main():
    css_id = 399
    path_hashes_5a = 'files/Passwords_5a.csv'
    path_hashes_5b = 'files/Passwords_5b.csv'
    path_passwords = 'files/rockyou-75.txt'

    rainbow_attack(path_hashes_5a, path_passwords, css_id)

    attack_results = hard_rainbow_attack(path_hashes_5b, path_passwords, css_id)

    if attack_results is not None:
        check_hashes(hard_encrypt(attack_results[0], attack_results[1], path_hashes_5b, css_id),
                     extract_password_hash(path_hashes_5b, css_id))


if __name__ == '__main__':
    main()
