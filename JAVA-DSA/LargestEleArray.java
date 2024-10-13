/*
 find the largest element in array 
 Time complexity : O(n)
*/

class LargestEleArray {
    public static void main(String args[]) {
        int n = 5;
        int arr[] = { 5, 3, 7, 2, 4 };

        int largest = arr[0];
        for ( int i = 0 ; i < n ; i++ ) {
            if ( arr[i] > largest ) {
                largest = arr[i];
            }
        }

        System.out.println("largest element --> " + largest);
    }
}