/*

    Find the second largest element in a array

 */

import java.util.Arrays;

class SecondLargestEleArray {
    // brute foce solution
    // time complexity: O(NlogN + N)
    public static int solution1(int arr[]) {
        Arrays.sort(arr);
        int n = arr.length;
        int largest = arr[n-1];
        
        for ( int i = arr.length - 1 ; i >= 0 ; i-- ) {
            if ( arr[i] != largest ){
                return arr[i];
            }
        }

        return -1;
    }

    // better solution
    // time complexity: O(2N)
    public static int solution2(int arr[]) {
        int largest = arr[0];
        int Slargest = -1;
        int n = arr.length;
        for ( int i = 0 ; i < n ; i++ ) {
            if ( arr[i] > largest ) {
                largest = arr[i];
            }
        }

        for ( int i = 0 ; i < n ; i++ ) {
            if ( arr[i] > Slargest && arr[i] != largest ) {
                Slargest = arr[i];
            }
        }

        return Slargest;
    }

    // optimal solution
    // time complexity : O(N)
    public static int solution3(int arr[]) {
        int largest = arr[0];
        int slargest = -1;
        int n = arr.length;

        for ( int i = 0 ; i < n ; i++ ) {
            if ( arr[i] > largest ) {
                slargest = largest;
                largest = arr[i];
            } else if ( arr[i] < largest && arr[i] > slargest ) {
                slargest = arr[i];
            }
        }

        return slargest;
    }

    public static void main(String[] args){
        int arr[] = { 1, 2, 4, 7, 7, 5 };

        System.out.println("brute solution -> " + solution1(arr));
        System.out.println("better solution --> " + solution2(arr));
        System.out.println("optimal solution --> " + solution3(arr));
    }
}