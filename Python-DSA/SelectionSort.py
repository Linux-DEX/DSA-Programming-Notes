def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[mini], arr[i] = arr[i], arr[mini]

def main():
    numberEle = int(input("Enter the number of elements: "))
    arr = []

    for _ in range(numberEle):
        arr.append(int(input()))

    selection_sort(arr)

    for element in arr:
        print(element, end=" ")

if __name__ == "__main__":
    main()
