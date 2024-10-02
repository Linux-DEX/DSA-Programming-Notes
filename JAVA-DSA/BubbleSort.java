import java.util.Scanner;

class BubbleSort {
    // this is optimized function when number is ascending order it will check and exit the code.
    static void bubble_sort(int arr[] , int n) {
        for ( int i = n - 1 ; i >= 0 ; i-- ) {
            int didSwap = 0;
            for ( int j = 0 ; j <= i - 1 ; j++ ) {
                if ( arr[j] > arr[j+1] ) {
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                    didSwap = 1;
                }
            }
            if ( didSwap == 0 ) {
                break;
            }
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int numberEle = sc.nextInt();
        int arr[] = new int[numberEle];
        
        for ( int i = 0 ; i < numberEle ; i++ ) {
            arr[i] = sc.nextInt();
        }

        bubble_sort(arr, numberEle);

        for ( int i = 0 ; i < numberEle ; i++ ) {
            System.out.print( arr[i] + " " );
        }

        sc.close();
    }
}