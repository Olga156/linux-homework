#!/usr/bin/env python3
import sys

def main():
    try:
        seconds = int(input("Введите количество секунд: "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        return

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    print(f"{hours:02}:{minutes:02}:{secs:02}")

if __name__ == "__main__":
    main()

