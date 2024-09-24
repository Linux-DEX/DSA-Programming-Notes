/* 

   Count elements of Array
 
*/

import java.util.Scanner;

class CountNumArray {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int arr[] = new int[n];
    for ( int i = 0 ; i < n ; i++ ){
      arr[i] = sc.nextInt();
    }

    // precompute
    int hash[] = new int[13]; 
    for ( int i = 0 ; i < n ; i++ ){
      hash[arr[i]] += 1;
    }

    int q = sc.nextInt();
    while( q-- > 0 ){
      int number = sc.nextInt();
      // fetch
      System.out.println(hash[number]);
    }
  }
}

// using Map 

// import java.util.HashMap;
// import java.util.Map;
// import java.util.Scanner;
//
// class CountNumArray {
//     public static void main(String args[]) {
//         Scanner sc = new Scanner(System.in);
//
//         int n = sc.nextInt();
//         Map<Integer, Integer> countMap = new HashMap<>();
//         
//         // Count occurrences
//         for (int i = 0; i < n; i++) {
//             int num = sc.nextInt();
//             countMap.put(num, countMap.getOrDefault(num, 0) + 1);
//         }
//
//         int q = sc.nextInt();
//         while (q-- > 0) {
//             int number = sc.nextInt();
//             // Fetch and print count
//             System.out.println(countMap.getOrDefault(number, 0));
//         }
//     }
// }


/*
 *
 * input format
 *
 * - array size 
 * - array elements 
 * - number of element you will be enter for fetch 
 * - enter element and output display after enter
 *
 * */
