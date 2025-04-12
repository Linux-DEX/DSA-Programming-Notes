"""

    find the second largest element in a array

"""

class SecondLargestEleArray:
    # brute force solution
    # time complexity: O(NlogN + N)
    @staticmethod
    def solution1(arr):
        arr.sort()
        largest = arr[-1]  

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] != largest:
                return arr[i]

        return -1

    # better solution
    # time complexity: O(2N)
    @staticmethod
    def solution2(arr):
        largest = arr[0]
        slargest = -1

        for i in range(len(arr)):
            if arr[i] > largest:
                largest = arr[i]

        for i in range(len(arr)):
            if arr[i] > slargest and arr[i] != largest:
                slargest = arr[i]

        return slargest

    # optimal solution
    # time complexity: O(N)
    @staticmethod
    def solution3(arr):
        largest = arr[0]
        slargest = -1

        for i in range(len(arr)):
            if arr[i] > largest:
                slargest = largest
                largest = arr[i]
            elif arr[i] < largest and arr[i] > slargest:
                slargest = arr[i]

        return slargest

if __name__ == "__main__":
    arr = [1, 2, 4, 7, 7, 5]

    print("brute solution ->", SecondLargestEleArray.solution1(arr))
    print("better solution ->", SecondLargestEleArray.solution2(arr))
    print("optimal solution ->", SecondLargestEleArray.solution3(arr))
