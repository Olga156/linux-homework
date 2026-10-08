#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("Ошибка: передайте число как аргумент командной строки.")
        print("Пример: python3 bases.py 255")
        return

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Аргумент должен быть целым числом.")
        return

    b_bin = bin(num)
    b_oct = oct(num)
    b_hex = hex(num)

    print(f"Исходное: {num}")
    print(f"Двоичная: {b_bin}")
    print(f"Восьмеричная: {b_oct}")
    print(f"Шестнадцатеричная: {b_hex}")

    print("\n--- Обратный перевод ---")
    print(f"{b_bin} -> {int(b_bin, 2)}")
    print(f"{b_oct} -> {int(b_oct, 8)}")
    print(f"{b_hex} -> {int(b_hex, 16)}")

if __name__ == "__main__":
    main()

