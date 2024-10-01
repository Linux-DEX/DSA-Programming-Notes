"""

   Character Hashing

"""

from collections import defaultdict


def main():
    s = input().strip()

    hash_map = defaultdict(int)

    for char in s:
        if char.isalpha():
            hash_map[char.lower()] += 1

    q = int(input().strip())
    for _ in range(q):
        c = input().strip()
        if c.isalpha():
            print(hash_map[c.lower()])
        else:
            print(0)


if __name__ == "__main__":
    main()
