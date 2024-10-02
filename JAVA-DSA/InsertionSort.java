import java.util.Scanner;

class InsertionSort {
    static void insertion_sort(int arr[], int n) {
        for ( int i = 0 ; i <= n - 1 ; i++ ) {
            int j = i; 
            while ( j > 0 && arr[j-1] > arr[j] ) {
                int temp = arr[j-1];
                arr[j-1] = arr[j];
                arr[j] = temp;
                j--;
            }
        }
    }

    public static void main( String args[] ) {
        Scanner sc = new Scanner(System.in);
        int numberEle = sc.nextInt();
        int arr[] = new int[numberEle];
        
        for ( int i = 0 ; i < numberEle ; i++ ) {
            arr[i] = sc.nextInt();
        }

        insertion_sort(arr, numberEle);

        for ( int i = 0 ; i < numberEle ; i++ ) {
            System.out.print( arr[i] + " " );
        }

        sc.close();
    }
}