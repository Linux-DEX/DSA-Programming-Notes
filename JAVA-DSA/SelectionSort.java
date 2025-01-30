import java.util.Scanner;

class SelectionSort {
  static void selection_sort( int arr[], int n) {
    for ( int i = 0 ; i <= n - 2 ; i++ ) {
      int mini = i; 
      for ( int j = i ; j <= n - 1 ; j++ ) {
        if ( arr[j] < arr[mini] ) {
          mini = j;
        }
      }
      int temp = arr[mini];
      arr[mini] = arr[i];
      arr[i] = temp;
    }
  }

  public static void main(String []args){
    Scanner sc = new Scanner(System.in);
    int numberEle = sc.nextInt();
    int arr[] = new int[numberEle];
    
    for ( int i = 0 ; i < numberEle ; i++ ) {
      arr[i] = sc.nextInt();
    }

    selection_sort(arr, numberEle);

    for ( int i = 0 ; i < numberEle ; i++ ) {
      System.out.print( arr[i] + " " );
    }

    sc.close();
  }
}
