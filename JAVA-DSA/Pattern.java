
class Pattern {
    public static void squareparttern() {
        for ( int i = 0 ; i <= 4 ; i++ ){
            for ( int j = 0 ; j <= 4 ; j++ ){
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public static void pattern_2() {
        for ( int i = 0 ; i <= 4 ; i++ ){
            for ( int j = 0 ; j <= i ; j++ ){
                System.out.print("* ");
            }
            System.out.println("");
        }
    }

    public static void pattern_3() {
        for ( int i = 0 ; i <= 4 ; i++ ){
            for ( int j = 1 ; j <= i ; j++ ){
                System.out.print( j + " ");
            }
            System.out.println("");
        }
    }

    public static void pattern_4() {
        for ( int i = 0 ; i <= 4 ; i++ ){
            for ( int j = 1 ; j <= 4 - i + 1 ; j++ ){
                System.out.print("* ");
            }
            System.out.println("");
        }
    }

    public static void pattern_5() {
        for ( int i = 0 ; i <= 4 ; i++ ){
            for ( int j = 1 ; j <= 4 - i + 1 ; j++ ){
                System.out.print(j + " ");
            }
            System.out.println("");
        }
    }

    public static void pattern_6( int n) {
        for ( int i = 0 ; i < n; i++ ){
            for ( int j = 0; j < n-i-1; j++) {
                System.out.print(" ");
            }
            for ( int j = 0; j < 2*i+1; j++ ){
                System.out.print("*");
            }
            for ( int j = 0; j < n-i-1; j++) {
                System.out.print(" ");
            }
            System.out.println("");
        }
    }

    public static void pattern_7( int n) {
        for ( int i = 0 ; i < n; i++ ){
            for ( int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            for ( int j = 0; j < 2*(n - i) - 1; j++ ){
                System.out.print("*");
            }
            System.out.println("");
        }
    }

    public static void pattern_8( int n) {
        for ( int i = 0 ; i <= 2*n-1; i++ ){
            int stars = i;
            if(i > n) stars = 2*n - i;
            for ( int j = 1; j <= stars; j++ ) {
                System.out.print("*");
            }
            System.out.println("");
        }
    }

    public static void pattern_9( int n) {
        int start = 1;
        for ( int i = 0 ; i <= 2*n-1; i++ ){
            if (i % 2 == 0) start = 1;
            else start = 0;
            for ( int j = 0 ; j < i ; j++ ){
                System.out.print(start);
                start = 1 - start;
            }
            System.out.println("");
        }
    }

    public static void pattern_10( int n ){
        int space = 2*(n -1);
        for ( int i = 0 ; i <= n ; i++ ){
            for ( int j = 1; j <= i; j++ ){
                System.out.print(j);
            }
            for ( int j = 1; j <= space; j++ ) {
                System.out.print(" ");
            }
            for ( int j = i; j >= 1; j-- ){
                System.out.print(j);
            }
            System.out.println();
            space -= 2;
        }
    }

    public static void pattern_11( int n ) {
        int num = 1;
        for ( int i = 0 ; i <= n ; i++ ){
            for ( int j = 1; j <= i; j++ ){
                System.out.print(num);
                num = num + 1;
            }
            System.out.println();
        }
    }

    public static void pattern_12( int n ) {
        for ( int i = 0 ; i <= n ; i++ ){
            for (char ch = 'A' ; ch <= 'A' + i; ch++ ){
                System.out.print(ch + " ");
            }
            System.out.println();
        }
    }

    public static void pattern_13( int n ) {
        for ( int i = 0 ; i <= n ; i++ ){
            for (char ch = 'A' ; ch <= 'A' + (n - i - 1); ch++ ){
                System.out.print(ch + " ");
            }
            System.out.println();
        }
    }

    public static void pattern_14( int n ) {
        for ( int i = 0 ; i < n ; i++ ){
            char ch = (char) ('A' + i);
            for ( int j = 0 ; j <= i ; j++ ){
                System.out.print(ch + " ");
            }
            System.out.println();
        }
    }

    public static void pattern_15( int n ) {
        int iniS = 0;
        for ( int i = 0 ; i < n ; i++ ){
            for ( int j = 1; j <= n-i; j++ ){
                System.out.print("*");
            }
            for ( int j = 0; j < iniS; j++ ){
                System.out.print(" ");
            }
            for ( int j = 1; j <= n-i; j++ ){
                System.out.print("*");
            }
            iniS += 2;
            System.out.println();
        }
        iniS = 2*(n - 1);
        for ( int i = 0 ; i < n ; i++ ){
            for ( int j = 1; j <= i; j++ ){
                System.out.print("*");
            }
            for ( int j = 0; j < iniS; j++ ){
                System.out.print(" ");
            }
            for ( int j = 1; j <= i; j++ ){
                System.out.print("*");
            }
            iniS -= 2;
            System.out.println();
        }
    }

    public static void pattern_16( int n ) {
        int space = 2*n - 2;
        for ( int i = 1 ; i < 2*n-1 ; i++ ){
            int stars = i;
            if ( i > n ) stars = 2*n - i;
            for ( int j = 1; j <= stars; j++ ){
                System.out.print("*");
            }
            for ( int j = 1; j < space; j++ ){
                System.out.print(" ");
            }
            for ( int j = 1; j <= stars; j++ ){
                System.out.print("*");
            }
            System.out.println();
            if ( i < n ) space -= 2;
            else space += 2;
        }
    }

    public static void pattern_17( int n ) {
        for ( int i = 0 ; i < n ; i++ ){
            for ( int j = 0 ; j < n ; j++ ) {
                if ( i == 0 || j == 0 || i == n-1 || j == n-1 ) {
                    System.out.print("*");
                }
                else System.out.print(" ");
            }
            System.out.println();
        }
    }

    public static void pattern_18( int n ) {
        for ( int i = 0 ; i < 2*n-1 ; i++ ){
            for ( int j = 0 ; j < 2*n-1 ; j++ ) {
                int top = i;
                int left = j;
                int right = (2*n - 2) -j;
                int down = (2*n - 2) -i;
                System.out.print( n - Math.min(Math.min(top, down), Math.min(left, right)));
            }
            System.out.println();
        }
    }

    public static void main(String args[]){
        int n = 5;
        squareparttern();
        System.out.println("");
        pattern_2();
        System.out.println("");
        pattern_3();
        System.out.println("");
        pattern_4();
        System.out.println("");
        pattern_5();
        System.out.println("");
        pattern_6(n);
        System.out.println("");
        pattern_7(n);
        System.out.println("");
        pattern_8(n);
        System.out.println("");
        pattern_9(n);
        System.out.println("");
        pattern_10(n);
        System.out.println("");
        pattern_11(n);
        System.out.println("");
        pattern_12(n);
        System.out.println("");
        pattern_13(n);
        System.out.println("");
        pattern_14(n);
        System.out.println("");
        pattern_15(n);
        System.out.println("");
        pattern_16(n);
        System.out.println("");
        pattern_17(n);
        System.out.println("");
        pattern_18(n);
    }
}