#!/usr/bin/env python3

def main():
    num_str = input("Введите трёхзначное число: ")
    if len(num_str) != 3 or not num_str.isdigit():
        print("Ошибка: введите ровно три цифры.")
        return

    num = int(num_str)
    d1 = num // 100
    d2 = (num // 10) % 10
    d3 = num % 10
    
    sum_digits = d1 + d2 + d3
    reversed_math = d3 * 100 + d2 * 10 + d1

    reversed_slice = num_str[::-1]

    print(f"Сумма цифр: {sum_digits}")
    print(f"Наоборот (через // и %): {reversed_math}")
    print(f"Наоборот (через срез): {reversed_slice}")

if __name__ == "__main__":
    main()

