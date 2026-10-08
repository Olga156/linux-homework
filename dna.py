#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("Ошибка: передайте строку ДНК в аргументы.")
        print("Пример: python3 dna.py CCATGCGTAA")
        return

    dna = sys.argv[1].upper()

    pairs = str.maketrans("ATCG", "TAGC")
    compl_dna = dna.translate(pairs)
    rev_compl_dna = compl_dna[::-1]

    rna = dna.replace("T", "U")

    start_codon_pos = dna.find("ATG")

    print(f"Исходная ДНК: {dna}")
    print(f"Обратно-комплементарная: {rev_compl_dna}")
    print(f"РНК: {rna}")
    print(f"Позиция старт-кодона ATG: {start_codon_pos}")

if __name__ == "__main__":
    main()

