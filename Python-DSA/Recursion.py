# NOTE: print name 5 times
# TC = O(N)
def func1(name, count):
    if count == 0:
        return
    print(name)
    func1(name, count - 1)


# NOTE: print from N to 1
# TC = O(N)
def func2(count):
    if count == 0:
        return
    print(count)
    func2(count - 1)


# NOTE: print linearly from 1 to N
# TC = O(N)
def func3(current, count):
    if current > count:
        return
    print(current)
    func3(current + 1, count)


# NOTE : Print Linearly from 1 to N ( but by backtrack )
def func4(i, n):
    if i < 1:
        return
    func4(i - 1, n)
    print(i)


# NOTE: Print from N to 1 ( by Backtrack )
def func5(i, n):
    if i > n:
        return
    func5(i + 1, n)
    print(i)


# NOTE: Sum of first N number using parameterised way
def func6(i, sum):
    if i < 1:
        print(sum)
        return
    func6(i - 1, sum + i)


# NOTE: Sum of first N number using parameterised way
def func7(num):
    if num == 0:
        return 0
    return num + func7(num - 1)


# NOTE: Reverse an array
def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


def func8(i, arr):
    n = len(arr)
    if i >= n // 2:
        return
    swap(arr, i, n - i - 1)
    func8(i + 1, arr)


# NOTE: fibonacci number using multile recursion calls
# TC = O(2^n)
def func9(n):
    if n <= 1:
        return n
    return func9(n - 1) + func9(n - 2)


if __name__ == "__main__":
    func1("Linux-DEX", 5)
    print()
    func2(5)
    print()
    func3(1, 5)
    print()
    func4(5, 5)
    print()
    func5(1, 5)
    print()
    func6(5, 0)
    print()
    print(func7(5))

    array = [1, 2, 3, 4, 5]
    func8(0, array)
    print(array)
    print()
    print(func9(8))

