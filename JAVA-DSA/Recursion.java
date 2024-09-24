
class Recursion {
    // NOTE: print name 5 times 
    // TC = O(N)
    static void func1(String name, int count) {
        if ( count == 0 ) {
            return;
        }
        System.out.println(name);
        func1(name, count - 1);
    }

    // NOTE: print linearly from 1 to N 
    // TC = O(N)
    static void func2(int count) {
        if ( count == 0 ) {
            return;
        }
        System.out.println(count);
        func2(count - 1);
    }

    // NOTE: print N to 1 
    // TC = O(N)
    static void func3(int current, int count) {
        if ( current > count ) {
            return;
        }
        System.out.println(current);
        func3( current + 1, count );
    }

    // NOTE: Print Linearly from 1 to N ( but by backtrack )
    static void func4( int i , int n ) {
        if ( i < 1 ) {
            return ;
        }
        func4(i - 1, n);
        System.out.println(i);
    }

    // NOTE: Print from N to 1 ( by Backtrack )
    static void func5(int i, int n) {
        if ( i > n ) return;
        func5(i + 1, n);
        System.out.println(i);
    }

    // NOTE: Sum of first N number using parameterised way 
    static void func6(int i, int sum) {
        if ( i < 1 ) {
            System.out.println(sum);
            return;
        }
        func6(i - 1, sum + i);
    }

    // NOTE: Sum of first N number using functional way 
    static int func7(int num) {
        if ( num == 0 ) {
            return 0;
        }
        return num + func7(num - 1);
    }

    // NOTE: Reverse an array 

    static void swap(int array[], int index1, int index2){
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    static void func8(int i, int arr[], int n) {
        if ( i >= n/2 ) return;
        swap(arr, i, n-i-1);
        func8(i+1, arr, n);
    }

    // NOTE: fibonacci number using multile recursion calls
    // TC = O(2^n)
    static int func9(int n) {
      if ( n <= 1 ) return n;
      return func9(n-1) + func9(n-2);
    }

    public static void main(String[] args) {
        func1("Linux-DEX", 5);
        System.out.println();
        func2(5);
        System.out.println();
        func3(1, 5);
        System.out.println();
        func4(5, 5);
        System.out.println();
        func5(1, 5);
        System.out.println();
        func6(5, 0);
        System.out.println();
        System.out.println(func7(5));
        
        int arr[] =  { 1, 2, 3, 4, 5 };
        func8(0, arr, arr.length);
        for ( int i = 0 ; i < arr.length ; i++ ) {
            System.out.print(arr[i] + " ");
        }

        System.out.println();
        System.out.println(func9(8));
    }
}
