/* 

Check if the array is sorted

*/

public class CheckArraySorted {
    public static boolean solution1( int[] arr ) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                return false;
            }
        }
        return true;
    }

    public static boolean solution2(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            if (arr[i] < arr[i - 1]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int[] array1 = {1, 2, 2, 3, 3, 4};
        int[] array2 = {1, 2, 1, 3, 4};

        System.out.println("Is array1 sorted (solution1)? -> " + solution1(array1));
        System.out.println("Is array2 sorted (solution2)? -> " + solution2(array2));
    }
}