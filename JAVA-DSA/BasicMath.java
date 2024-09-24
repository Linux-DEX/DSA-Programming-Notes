import java.util.Vector;
import java.util.Collections;

class BasicMath {
    public static int countDigits(int num) {
        if ( num == 0 ) return 1;
        num = Math.abs(num);
        int count = 0;
        while ( num > 0 ) {
            int lastDigit = num % 10;
            count = count + 1;
            num = num / 10;
        }
        return count;
    }

    public static int reverseNumber(int num) {
        int revNum = 0;
        while ( num > 0 ) {
            int lastDigit = num % 10;
            revNum = (revNum * 10) + lastDigit;
            num = num / 10;
        }
        return revNum;
    }

    public static boolean palindrome(int num) {
        if (num < 0 ) return false;
        int originalNum = num;
        int revNum = 0;
        while ( num > 0 ) {
            int lastDigit = num % 10;
            revNum = (revNum * 10) + lastDigit;
            num = num / 10;
        }
        return originalNum == revNum;
    }

    public static boolean armstrongNumber(int num) {
        if (num < 0 ) return false;
        int sum = 0;
        int originalNum = num;
        int numberOfDigits = String.valueOf(num).length();
        while ( num > 0 ) {
            int lastDigit = num % 10;
            sum += Math.pow(lastDigit, numberOfDigits);
            num = num / 10;
        }
        return sum == originalNum;
    }

    public static void printDivisors(int num) {
        for ( int i = 1; i <= num; i++ ){
            if ( num%i == 0 ) {
                System.out.print(i + " ");
            }
        }
    }

    public static void printDivisorsOther(int num) {
        Vector<Integer> ls = new Vector<Integer>();
        for ( int i = 1; i*i <= num; i++ ){
            if ( num%i == 0 ) {
                ls.add(i);
                if ( (num/i) != i ) {
                    ls.add(num/i);
                }
            }
        }
        Collections.sort(ls);
        System.out.println(ls);
    }

    public static void primeNumber(int num) {
        int count = 0;
        for ( int i = 1; i*i <= num; i++ ){
            if ( num%i == 0 ) {
                count++;
                if ( (num/i) != i ) {
                    count++;
                }
            }
        }
        if ( count == 2 ) System.out.println("prime num : " + num + " true");
        else System.out.println("prime num: " + num + " false");
    }

    public static void main(String args[]) {
        int num = 7789;
        int num2 = 141;
        int num3 = 1634;
        System.out.println("count digits -> " + countDigits(num) );
        System.out.println("reverse number -> " + reverseNumber(num));
        System.out.println("palindrome : " + num2 + " -> " + palindrome(num2));
        System.out.println("Armstrong number : " + num3 + " -> " + armstrongNumber(num3));
        System.out.println("Divisors of number" + num2);
        printDivisors(num2);
        System.out.println();
        printDivisorsOther(num2);
        primeNumber(17);
    }
}