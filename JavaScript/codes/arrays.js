// defining array
/*
const linux = ["Arch", "ubantu", "debian", "fedora"];

const linux = [];
linux[0] = "Arch";
linux[1] = "ubantu";
linux[2] = "debian";

const linux = new Array('arch', 'ubantu', 'debian', 'fedora')
*/

const linuxs = ["Arch", "ubantu", "debian", "fedora"];

// accessing array element
let linux = linuxs[0];

// changing an array element
linuxs[0] = "openSUSE";

// converting an array to string
let str_linuxs = linuxs.toString();

// Arrays are a special type of objects. The typeof operator in JavaScript returns "object" for arrays.
console.log("array type", typeof linuxs);
let a = [6, 10, 4, 1, 5, 8];
console.log("array lenght", a.length);
console.log("array sort", a.sort());

linuxs.push("blackarch"); // add new element to linuxs
linuxs.pop(); // remove element from linuxs

// how to recognize an array
let type = typeof linuxs;
let isArr = Array.isArray(linuxs);
let otherIsArr = linuxs instanceof Array;

console.log(`array type ${type}, isArr ${isArr}, other isArr ${otherIsArr}`);

console.log("ele at 2 index", linuxs.at(2));

console.log("join all ele of array", linuxs.join("^"));

console.log(linuxs.shift()); // removes the first array element and shifts all other element to a lower index.

console.log(linuxs.unshift("lemon")); // adds a new ele to an array and unshifts older elements

delete linuxs[0]; // using delete leave undefined holes in the array

const arr1 = ["Cecilie", "Lone"];
const arr2 = ["Emil", "Tobias", "Linus"];
const arr3 = ["Robin", "Morgan"];
const myChildren = arr1.concat(arr2, arr3);

console.log(myChildren);

myChildren.copyWithin(2, 0); // copy to index 2, the ele from index 0 to 2
console.log(myChildren);

const myArr = [
  [1, 2],
  [3, 4],
  [5, 6],
];
const newArr = myArr.flat(); // create new array with sub-array ele concatenated to a specified depth
console.log(newArr);

// splice()
/* 
- can be used to add new items to an array 
- returns an array with the deleted items
*/
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.splice(2, 0, "Lemon", "Kiwi");
console.log(fruits);

const months = ["Jan", "Feb", "Mar", "Apr"];
const spliced = months.toSpliced(0, 1); // a safe way to splice an array without alterning the original array.
console.log(spliced);

// slice()
/*
- method slices out a piece of an array into a new array
*/
const citrus = fruits.slice(1, 3);
console.log(citrus);

console.log(months.indexOf("Apr")); // return index of element

console.log(myChildren.lastIndexOf("Cecilie")); // return the position of the last occurrence of the specified element.

console.log(months.includes("Feb")); // check if an ele is present in an array

console.log("months -", months.reverse());
