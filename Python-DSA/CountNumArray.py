"""

    Count elements of Array

"""


# using list
def main():
    n = int(input())
    arr = list(map(int, input().split()))

    max_value = max(arr) if arr else 0
    count = [0] * (max_value + 1)

    for number in arr:
        count[number] += 1

    q = int(input())
    for _ in range(q):
        number = int(input())
        print(count[number] if 0 <= number <= max_value else 0)


# using dictionary
# def main():
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     count = {}
#     for number in arr:
#         count[number] = count.get(number, 0) + 1
#
#     q = int(input())
#     for _ in range(q):
#         number = int(input())
#         print(count.get(number, 0))


if __name__ == "__main__":
    main()

"""
 input format

 - array size 
 - array elements 
 - number of element you will be enter for fetch 
 - enter element and output display after enter
"""
