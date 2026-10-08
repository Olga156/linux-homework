#!/usr/bin/env python3

def main():
    s = input("Введите строку: ")
    if not s:
        print("Строка пустая.")
        return

    length = len(s)
    first = s[0]
    last = s[-1]
    middle = s[length // 2]
    every_second = s[::2]
    reversed_str = s[::-1]
    is_palindrome = s == reversed_str

    print(f"Длина: {length}")
    print(f"Первый символ: {first}")
    print(f"Последний символ: {last}")
    print(f"Средний символ: {middle}")
    print(f"Каждый второй: {every_second}")
    print(f"Наоборот: {reversed_str}")
    print(f"Палиндром: {is_palindrome}")

if __name__ == "__main__":
    main()

