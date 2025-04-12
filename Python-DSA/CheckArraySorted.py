"""

    Check if the array is sorted

"""

class CheckArraySorted:
    @staticmethod
    def solution1(arr):
        return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

    @staticmethod
    def solution2(arr):
        n = len(arr)
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                return False
        return True


if __name__ == "__main__":
    array1 = [1, 2, 2, 3, 3, 4]
    array2 = [1, 2, 1, 3, 4]

    print("is sorted ->", CheckArraySorted.solution1(array1))
    print("is sorted ->", CheckArraySorted.solution2(array2))
