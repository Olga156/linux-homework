#!/usr/bin/env python3

def main():
    a = 37
    b = 73
    print(f"До перестановки: a = {a} (id: {id(a)}), b = {b} (id: {id(b)})")

    a, b = b, a
    print(f"Способ 1: a = {a} (id: {id(a)}), b = {b} (id: {id(b)})")

    a, b = b, a 

    tmp = a
    a = b
    b = tmp
    print(f"Способ 2: a = {a} (id: {id(a)}), b = {b} (id: {id(b)})")

if __name__ == "__main__":
    main()

