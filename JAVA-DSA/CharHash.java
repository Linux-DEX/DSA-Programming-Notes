/* 

   Character Hashing

*/

import java.util.Scanner;

class CharHash {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] hash = new int[26];

        String s = sc.nextLine();
        for (char currentChar : s.toCharArray()) {
            if (Character.isLowerCase(currentChar)) {
                hash[currentChar - 'a']++;
            } else if (Character.isUpperCase(currentChar)) {
                hash[Character.toLowerCase(currentChar) - 'a']++;
            }
        }

        int q = sc.nextInt();
        while (q-- > 0) {
            char c = sc.next().charAt(0);
            if (Character.isLetter(c)) {
                System.out.println(hash[Character.toLowerCase(c) - 'a']);
            } else {
                System.out.println(0);
            }
        }

        sc.close(); 
    }
}

