"""

    Remove duplicates from sorted array

"""

class RemoveDuplicateSortedArray:
    # Brute force solution
    # Time complexity: NlogN + N
    @staticmethod
    def solution1(arr):
        unique_elements = set(arr)

        arr[:len(unique_elements)] = sorted(unique_elements)

        print("Brute force solution:")
        for i in range(len(unique_elements)):
            print(arr[i], end=" ")
        print()

    # Optimal solution
    # Time complexity: O(N)
    @staticmethod
    def solution2(arr):
        index = 0
        for j in range(1, len(arr)):
            if arr[index] != arr[j]:
                index += 1
                arr[index] = arr[j]

        print("Optimal solution:")
        for i in range(index + 1):
            print(arr[i], end=" ")
        print()

    @staticmethod
    def solution3(arr):
        unique_set = set(arr)
        unique_list = list(unique_set)
        print(f"python way - {unique_list}")

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]

    arr1 = arr.copy()
    RemoveDuplicateSortedArray.solution1(arr1)
    RemoveDuplicateSortedArray.solution2(arr)
    RemoveDuplicateSortedArray.solution3(arr1)
