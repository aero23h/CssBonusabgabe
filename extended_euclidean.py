
def extended_euclidean_algo(a, b):
    x_old, x = 1, 0
    y_old, y = 0, 1

    output = [f"{'a':^10} {'b':^10} {'q':^10} {'x':^10} {'y':^10}", "-" * 60,
              f"{a:^10} {b:^10} {'-':^10} {x_old:^10} {y_old:^10}"]

    while b != 0:
        q = a // b
        a, b = b, a % b
        x, x_old = x_old - q * x, x
        y, y_old = y_old - q * y, y

        output.append(f"{a:^10} {b:^10} {q:^10} {x_old:^10} {y_old:^10}")

    return a, x_old, y_old, output


def main():
    matrikelnummer = 2521215
    zahl = 2024

    # ggT Berechnung
    ggt, x, y, output_lines = extended_euclidean_algo(matrikelnummer, zahl)

    # Ausgabe der Ergebnisse
    for line in output_lines:
        print(line)

    print(f"\nDer ggT von {matrikelnummer, zahl} ist: {ggt}")
    print(f"Koeffizienten x und y sind: x = {x}, y = {y}")


if __name__ == '__main__':
    main()


