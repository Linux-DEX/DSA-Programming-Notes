import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

public class RemoveDuplicateSortedArray {

    // Brute force solution
    // Time complexity: O(NlogN + N)
    public static void solution1(int[] arr) {
        Set<Integer> uniqueElements = new HashSet<>();
        
        for (int num : arr) {
            uniqueElements.add(num);
        }

        Integer[] uniqueArray = uniqueElements.toArray(new Integer[0]);
        Arrays.sort(uniqueArray);

        System.out.println("Brute force solution:");
        for (int i = 0; i < uniqueArray.length; i++) {
            System.out.print(uniqueArray[i] + " ");
        }
        System.out.println();
    }

    // Optimal solution
    // Time complexity: O(N)
    public static void solution2(int[] arr) {
        int index = 0;
        
        for (int j = 1; j < arr.length; j++) {
            if (arr[index] != arr[j]) {
                index++;
                arr[index] = arr[j];
            }
        }

        System.out.println("Optimal solution:");
        for (int i = 0; i <= index; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void solution3(int[] arr) {
        Set<Integer> uniqueSet = new HashSet<>();
        
        for (int num : arr) {
            uniqueSet.add(num);
        }

        System.out.println("Python way - " + uniqueSet);
    }

    public static void main(String[] args) {
        int[] arr = {1, 1, 2, 2, 2, 3, 3};

        int[] arr1 = Arrays.copyOf(arr, arr.length);
        solution1(arr1);

        solution2(arr);

        solution3(arr);
    }
}
