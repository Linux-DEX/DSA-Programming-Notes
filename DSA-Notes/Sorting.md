# Sorting Algorithm

## Selection Sort

**Step of the selection sort algorithm**

1.  Start with the first element as the initial position.
2.  Find the smallest element in the unsorted portion of the array.
3.  Swap this smallest element with the first unsorted element.
4.  Move the boundary of the sorted portion one element forward.
5.  Repeat steps 2-4 for the remaining unsorted elements until the entire array is sorted.

![selection sort](./img/selectionSort.png)

**Code**

- [java](./../JAVA-DSA/SelectionSort.java)
- [python](./../Python-DSA/SelectionSort.py)

**Time Complexity**

- best , worst, and average time complexity is `O(N^2)`

## Bubble Sort

**Step of the Bubble sort algorithm**

1. Start at the first element of the array.
2. Compare the current element with the next element.
3. If the current element is greater than the next element, swap them.
4. Move to the next pair of elements and repeat the comparison and swap if needed.
5. After each complete pass through the array, the largest unsorted element is placed at its correct position at the end of the array.
6. Repeat the above process of a pass for the remaining unsorted elements until the entire array is sorted.

![Bubble sort](./img/bubblesort.png)

**Code**

- [java](./../JAVA-DSA/BubbleSort.java)
- [python](./../Python-DSA/BubbleSort.py)

**Time Complexity**

- Worst or Average time complexity is `O(N^2)`
- Best time complexity is `O(N)`

## Insertion Sort

**Step of the Insertion sort algorithm**

1. We start with second element of the array as first element in the array is assumed to be sorted.
2. Compare second element with the first element and check if the second element is smaller then swap them.
3. Move to the third element and compare it with the second element, then the first element and swap as necessary to put it in the correct position among the first three elements.
4. Continue this process, comparing each element with the ones before it and swapping as needed to place it in the correct position among the sorted elements.
5. Repeat until the entire array is sorted.

![Insertion Sort](./img/insertionsort.png)
