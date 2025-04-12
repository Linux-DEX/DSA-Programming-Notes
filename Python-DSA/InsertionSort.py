def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        j = i 
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

def main():
    number_ele = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements: ").split()))
    insertion_sort(arr)
    print("Sorted array:", ' '.join(map(str, arr)))

if __name__ == "__main__":
    main()
