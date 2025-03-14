const arr1 = [ 5, 12, 8, 130, 44 ]

// at() -> return element at index
/* 
The at() method of Array instances takes an integer value and returns the item at that index, allowing for positive and negative integers. Negative integers count back from the last item in the array.
*/
let index = 2
console.log(`item at index ${index} -> ${arr1.at(index)}`) // output: 8

index = -2
console.log(`item at index ${index} -> ${arr1.at(index)}`) // output: 130

index = 8
console.log(`item at index ${index} -> ${arr1.at(index)}`) // undefined


// concat() -> merge array & return new array
/*
The concat() method of Array instances is used to merge two or more arrays. This method does not change the existing arrays, but instead returns a new array.
*/
const arrconcat1 = ["a", "b", "c"]
const arrconcat2 = ["d", "e", "f"]
const arrconcat3 = arrconcat1.concat(arrconcat2);

console.log(arrconcat3) // output: ["a", "b", "c", "d", "e", "f"]

const arrconcat4 = arr1.concat(arrconcat1, arrconcat2)

console.log(arrconcat4) // output: [5, 12, 8, 130, 44, "a", "b", "c", "d", "e", "f"]


// copyWithin() 
/*
The copyWithin() method of Array instances shallow copies part of this array to another location in the same array and returns this array without modifying its length.

# syntax 
copyWithin(target, start)
copyWithin(target, start, end)
*/

const arrCopyWithin = ["a", "b", "c", "d", "e"]

// Copy to index 0 the element at index 3
console.log(arrCopyWithin.copyWithin(0, 3, 4)); // output: ["d", "b", "c", "d", "e"]

// Copy to index 1 all elements from index 3 to the end
console.log(arrCopyWithin.copyWithin(1, 3)); // output: ["d", "d", "e", "d", "e"]


// entries() -> return new iterator object , contains key/value pairs
/*
The entries() method of Array instances returns a new array iterator object that contains the key/value pairs for each index in the array.
*/

const arrEntries = ["a", "b", "c", "d", "e"]

const iterator1 = arrEntries.entries()

console.log(iterator1.next().value) // output: [ 0, "a" ]

console.log(iterator1.next().value) // output: [ 1, "b" ]

for (const [index, element] of arrEntries.entries()) {
  console.log(index, element);
}
/*
 # output 
 0 a
 1 b
 2 c
 3 d 
 4 e
 */


// every() -> whether all ele in array pass the test
/*
The every() method of Array instances tests whether all elements in the array pass the test implemented by the provided function. It returns a Boolean value.
*/

const isBelowThreshold = (currentValue) => currentValue < 40;

const arrEvery = [1, 30, 39, 29, 10, 13];

console.log(arrEvery.every(isBelowThreshold)); // output: true


// fill()
/*
The fill() method of Array instances changes all elements within a range of indices in an array to a static value. It returns the modified array.
 */

const arrfill = [1, 2, 3, 4];

console.log(arrfill.fill(0, 2, 4)); // output: [1, 2, 0, 0]
console.log(arrfill.fill(5, 1)); // output: [1, 5, 5, 5]
console.log(arrfill.fill(6)); // output: [6, 6, 6, 6]


// filter() 
/*
The filter() method of Array instances creates a shallow copy of a portion of a given array, filtered down to just the elements from the given array that pass the test implemented by the provided function.
*/

const wordFilter = ["spray", "elite", "exuberant", "destruction", "present"];

const resultFilter = wordFilter.filter((word) => word.length > 6);

console.log(resultFilter) // output: ["exuberant", "destruction", "present"]


// find()
/* 
The find() method of Array instances returns the first element in the provided array that satisfies the provided testing function. If no values satisfy the testing function, undefined is returned.
*/

const arrFind = [5, 12, 8, 130, 44];

const resultFind = arrFind.find((element) => element > 10);

console.log(resultFind); // output: 12


// findIndex() 
/*
The findIndex() method of Array instances returns the index of the first element in an array that satisfies the provided testing function. If no elements satisfy the testing function, -1 is returned.
*/


const arrFindIndex = [5, 12, 8, 130, 44];

const isLargeNumber = (element) => element > 13;

console.log(arrFindIndex.findIndex(isLargeNumber)); // output: 3


// findLast() 
/* 
The findLast() method of Array instances iterates the array in reverse order and returns the value of the first element that satisfies the provided testing function. If no elements satisfy the testing function, undefined is returned.
*/

const arrFindLast = [5, 12, 50, 130, 44];

const resultFindLast = arrFindLast.findLast((element) => element > 45);

console.log(resultFindLast); // output: 130


// findLastIndex()
/*
The findLastIndex() method of Array instances iterates the array in reverse order and returns the index of the first element that satisfies the provided testing function. If no elements satisfy the testing function, -1 is returned.
*/

const arrFindLastIndex = [5, 12, 50, 130, 44];

const funcFindLastIndex = (element) => element > 45;

console.log(arrFindLastIndex.findLastIndex(funcFindLastIndex)); // output: 3


// flat()
/*
The flat() method of Array instances creates a new array with all sub-array elements concatenated into it recursively up to the specified depth.
*/

const arrFlat = [0, 1, 2, [3, 4]];

console.log(arrFlat.flat()); // output: [0, 1, 2, 3, 4]


// flatMap()
/*
The flatMap() method of Array instances returns a new array formed by applying a given callback function to each element of the array, and then flattening the result by one level. It is identical to a map() followed by a flat() of depth 1 (arr.map(...args).flat()), but slightly more efficient than calling those two methods separately.
*/

const arrFlatMap = [1, 2, 1];

const resultFlatMap = arrFlatMap.flatMap((num) => (num === 2 ? [2, 2] : 1));

console.log(resultFlatMap); // output: [1, 2, 2, 1]


// forEach()
/*
The forEach() method of Array instances executes a provided function once for each array element.
*/

const arrForEach = ["a", "b", "c"];

arrForEach.forEach((element) => console.log(element));

/*
    output:
    a
    b
    c
*/


// includes()
/*
The includes() method of Array instances determines whether an array includes a certain value among its entries, returning true or false as appropriate.
*/

const arrIncludes = ["arch", "debian", "fedora"];

console.log(arrIncludes.includes("arch")); // output: true


// indexOf()
/*
The indexOf() method of Array instances returns the first index at which a given element can be found in the array, or -1 if it is not present.
*/

const arrIndexOf = ["ant", "bison", "camel", "duck", "bison"];

console.log(arrIndexOf.indexOf("bison")) // output: 1
// start from index 2
console.log(arrIndexOf.indexOf("bison", 2)) // output: 4
console.log(arrIndexOf.indexOf("giraffe")) // output: -1


// join()
/*
The join() method of Array instances creates and returns a new string by concatenating all of the elements in this array, separated by commas or a specified separator string. If the array has only one item, then that item will be returned without using the separator.
*/

const arrJoin = ["Fire", "Air", "Water"];

console.log(arrJoin.join(" ")); // output: Fire Air Water
console.log(arrJoin.join("-")); // output: Fire-Air-Water


// keys()
/*
The keys() method of Array instances returns a new array iterator object that contains the keys for each index in the array.
*/

const arrKeys = ["a", "b", "c"];
const iterator2 = arrKeys.keys();

for (const key of iterator2){
  console.log(key);
}

/*
  output:
  0
  1
  2
*/


// lastIndexOf()
/*
The lastIndexOf() method of Array instances returns the last index at which a given element can be found in the array, or -1 if it is not present. The array is searched backwards, starting at fromIndex.
*/

const animals = ["Dodo", "Tiger", "Penguin", "Dodo"];

console.log(animals.lastIndexOf("Dodo")); // output: 3
console.log(animals.lastIndexOf("Tiger")); // output: 1


// map()
/*
The map() method of Array instances creates a new array populated with the results of calling a provided function on every element in the calling array.
*/

const arrMap = [1, 4, 9, 16];

const resultMap = arrMap.map((x) => x * 2);

console.log(resultMap) // output: [ 2, 8, 18, 32 ]


// pop()
// The pop() method of Array instances removes the last element from an array and returns that element. This method changes the length of the array.

const plants = ["broccoli", "cauliflower", "cabbage", "kale", "tomato"];

console.log(plants.pop()); // output: tomato
console.log(plants) // output: ["broccoli", "cauliflower", "cabbage", "kale"];


// push()
// The push() method of Array instances adds the specified elements to the end of an array and returns the new length of the array.

const animalsarr = ["pigs", "goats", "sheep"];

const count = animalsarr.push("cows");
console.log(count); // output: 4
console.log(animalsarr); // output: Array ["pigs", "goats", "sheep", "cows"]


// reduce()
// The reduce() method of Array instances executes a user-supplied "reducer" callback function on each element of the array, in order, passing in the return value from the calculation on the preceding element. The final result of running the reducer across all elements of the array is a single value.

const arrReduce = [1, 2, 3, 4];

// 0 + 1 + 2 + 3 + 4
const initialValue = 0;
const sumWithInitial = arrReduce.reduce(
  (accumulator, currentValue) => accumulator + currentValue,
  initialValue,
);

console.log(sumWithInitial); // output: 10


// reduceRight()
// The reduceRight() method of Array instances applies a function against an accumulator and each value of the array (from right-to-left) to reduce it to a single value.

const arrReduceRight = [
  [0, 1],
  [2, 3],
  [4, 5],
];

const resultReduceRight = arrReduceRight.reduceRight((accumulator, currentValue) =>
  accumulator.concat(currentValue),
);

console.log(resultReduceRight); // output: Array [4, 5, 2, 3, 0, 1]


// reverse() 
// The reverse() method of Array instances reverses an array in place and returns the reference to the same array, the first array element now becoming the last, and the last array element becoming the first. In other words, elements order in the array will be turned towards the direction opposite to that previously stated.

const arrReverse = ["one", "two", "three"];
console.log("arrReverse:", arrReverse); // output: "arrReverse:" ["one", "two", "three"]

const reversed = arrReverse.reverse();
console.log("reversed:", reversed); // output: "reversed:" ["three", "two", "one"]

// Careful: reverse is destructive -- it changes the original array.
console.log("arrReverse:", arrReverse); // output: "arrReverse:" ["three", "two", "one"]


// shift()
// The shift() method of Array instances removes the first element from an array and returns that removed element. This method changes the length of the array.

const arrShift = [1, 2, 3];

const firstElement = arrShift.shift();

console.log(arrShift); // output: [2, 3]
console.log(firstElement); // output: 1


// slice
// The slice() method of Array instances returns a shallow copy of a portion of an array into a new array object selected from start to end (end not included) where start and end represent the index of items in that array. The original array will not be modified.

const arrSlice = ["ant", "bison", "camel", "duck", "elephant"];

console.log(arrSlice.slice(2)); // output: ["camel", "duck", "elephant"]
console.log(arrSlice.slice(2, 4)); // output: ["camel", "duck"]
console.log(arrSlice.slice(1, 5)); // output: ["bison", "camel", "duck", "elephant"]
console.log(arrSlice.slice(-2)); // output: ["duck", "elephant"]
console.log(arrSlice.slice(2, -1)); // output: ["camel", "duck"]
console.log(arrSlice.slice()); // output: ["ant", "bison", "camel", "duck", "elephant"]


// some()
// The some() method of Array instances tests whether at least one element in the array passes the test implemented by the provided function. It returns true if, in the array, it finds an element for which the provided function returns true; otherwise it returns false. It doesn't modify the array.

const arrSome = [1, 2, 3, 4, 5];

const even = (element) => element % 2 === 0;

console.log(arrSome.some(even)); // output: true


// sort()
// The sort() method of Array instances sorts the elements of an array in place and returns the reference to the same array, now sorted. The default sort order is ascending, built upon converting the elements into strings, then comparing their sequences of UTF-16 code unit values.

const months = ["March", "Jan", "Feb", "Dec"];
months.sort();
console.log(months); // output: ["Dec", "Feb", "Jan", "March"]

const array1 = [1, 30, 4, 21, 100000];
array1.sort();
console.log(array1); // output: [1, 100000, 21, 30, 4]


// splice()
// The splice() method of Array instances changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.

const arrSplice = ["Jan", "March", "April", "June"];
arrSplice.splice(1, 0, "Feb");
// Inserts at index 1
console.log(arrSplice); // output: ["Jan", "Feb", "March", "April", "June"]


// toLocaleString()
// The toLocaleString() method of Array instances returns a string representing the elements of the array. The elements are converted to strings using their toLocaleString methods and these strings are separated by a locale-specific string (such as a comma ",").

const arrToLocaleStr = [1, "a", new Date("21 Dec 1997 14:12:00 UTC")];
const localeString = arrToLocaleStr.toLocaleString("en", { timeZone: "UTC" });

console.log(localeString);
// output: "1,a,12/21/1997, 2:12:00 PM",


// toReversed()
// The toReversed() method of Array instances is the copying counterpart of the reverse() method. It returns a new array with the elements in reversed order.

const item = [1, 2, 3];

console.log(item.toReversed()); // output: [3, 2, 1]


// toSorted()
// The toSorted() method of Array instances is the copying version of the sort() method. It returns a new array with the elements sorted in ascending order.

const arrToSorted = ["Mar", "Jan", "Feb", "Dec"];
const sortedarr = arrToSorted.toSorted();
console.log(sortedarr); // ['Dec', 'Feb', 'Jan', 'Mar']


// toSpliced()
// The toSpliced() method of Array instances is the copying version of the splice() method. It returns a new array with some elements removed and/or replaced at a given index.

const arrToSpliced = ["Jan", "Mar", "Apr", "May"];

// Inserting an element at index 1
const arrToSpliced2 = arrToSpliced.toSpliced(1, 0, "Feb");
console.log(arrToSpliced2); // ["Jan", "Feb", "Mar", "Apr", "May"]


// toString()
// The toString() method of Array instances returns a string representing the specified array and its elements.

const array = [1, 2, "a", "1a"];
console.log(array.toString()); // output: "1,2,a,1a"


// unshift()
// The unshift() method of Array instances adds the specified elements to the beginning of an array and returns the new length of the array.

const arrUnshift = [1, 2, 3];

console.log(arrUnshift.unshift(4, 5)); // output: 5
console.log(arrUnshift); // output: Array [4, 5, 1, 2, 3]


// values()
// The values() method of Array instances returns a new array iterator object that iterates the value of each item in the array.

const arrValues = ["a", "b", "c"];
const iterator = arrValues.values();

for (const value of iterator) {
  console.log(value);
}
/*
  output:
  a
  b
  c
*/


// with()
// The with() method of Array instances is the copying version of using the bracket notation to change the value of a given index. It returns a new array with the element at the given index replaced with the given value.

const arr = [1, 2, 3, 4, 5];
console.log(arr.with(2, 6)); // [1, 2, 6, 4, 5]
