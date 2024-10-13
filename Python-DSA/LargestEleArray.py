"""

find the largest element in the array 
Time complexity: O(n)

"""

arr =  [ 5, 3, 7, 2, 4 ] 

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print(largest)

# other way

largestEle = max(arr)
print(largestEle)