#!/usr/bin/env python3

def main():
    try:
        celsius = float(input("Введите температуру в °C: "))
    except ValueError:
        print("Ошибка ввода.")
        return

    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15

    print(f"{celsius} -> {fahrenheit:.1f}°F, {kelvin:.2f} K")

if __name__ == "__main__":
    main()

