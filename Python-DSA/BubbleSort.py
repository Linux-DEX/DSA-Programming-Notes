# this is optimized function when number is ascending order it will check and exit the code.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1 , -1, -1):
        didSwap = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                didSwap = 1
            if didSwap == 0:
                break

def main():
    number_ele = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements: ").split()))
    bubble_sort(arr)
    print("Sorted array:", ' '.join(map(str, arr)))

if __name__ == "__main__":
    main()