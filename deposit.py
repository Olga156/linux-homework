#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 4:
        print("Ошибка. Использование: python3 deposit.py [сумма] [ставка %] [лет]")
        print("Пример: python3 deposit.py 100000 12 3")
        return

    try:
        principal = float(sys.argv[1])
        rate = float(sys.argv[2]) / 100
        years = int(sys.argv[3])
    except ValueError:
        print("Некорректный формат аргументов.")
        return

    total = principal * (1 + rate) ** years

    print(f"{int(principal)} {int(rate*100)} {years} -> {total:.2f}")

if __name__ == "__main__":
    main()

