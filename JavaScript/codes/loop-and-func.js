const arrayVal = ["Hi", "Hello", 900, 23, true, "JavaScript"];
const objVal = {
  brand: "OD",
  model: "Q7",
  color: "Black",
};
const str = "linux-dex";
const map = new Map();
map.set("one", 1);
map.set("second", 2);
map.set("third", 3);
const number = [1, 2, 3, 4, 5, 6, 7, 8, 9];

// for loop is used to execute a block of code repeteatedly until a specified condition evaluates to false.
console.log("\nfor loop");
for (let count = 0; count < arrayVal.length; count++) {
  console.log(`count val - ${count} - ${arrayVal[count]}`);
}

// for...in loop in js is used to loop through an object's properties.
console.log("\nfor in");
for (let key in objVal) {
  console.log(`car key: ${key} value: ${objVal[key]}`);
}

for (let key in arrayVal) {
  console.log(`array key: ${key} value: ${arrayVal[key]}`);
}

// for...of loop in js is used to traverse elements of the iterable object. iterable object includes arrays, strings, maps, sets and generators.
console.log("\nfor of");
for (let ele of str) {
  console.log("element of string", ele);
}

for (let ele of arrayVal) {
  console.log("element of array", ele);
}

for (let [key, val] of map) {
  console.log(`obj value key: ${key} value: ${val}`);
}

// map() creates a new array by applying a function to each element in the array.
console.log("\nmap func");
// const newMapFuncVal = number.map((val) => val * 2);
const newMapFuncVal = number.map((val) => {
  let newVal = val * 4;
  newVal = newVal + val;
  return newVal;
});
console.log("map func value", newMapFuncVal);

// filter() creates a new array with all elements that pass the test implemented by the provided functions.
console.log("\nfilter func");
// const newFilterFuncVal = number.filter((num) => num % 2 === 0);
const newFilterFuncVal = arrayVal.filter((val) => {
  let newVal = val !== "Hi" && val !== 23;
  return newVal;
});
console.log("filter func value", newFilterFuncVal);

// reducer() applies a function to each element in the array(from left to right) to reduce it to a single value.
console.log("\nreduce func");
const newReduceVal = number.reduce((acc, num) => acc + num, 0);
console.log("reduce func value", newReduceVal);

// find() returns the first element in the array that satisfies the provided testing function.
console.log("\nfind func");
const firstEven = number.find((num) => num % 3 === 0);
console.log(firstEven);

// forEach() executes a provided function once for each array element.
console.log("\nfindEach func");
number.forEach((element) => {
  console.log(element * 2);
});

// some() tests whether at least one element in the array passes the test implemented by the provided function.
console.log("\nsome func");
const hasEven = number.some((num) => num % 2 === 0);
console.log("some func output -", hasEven);

// every() tests whether all elements in the array pass the test implemented by the provided function.
console.log("\nevery func");
const allEven = number.every((num) => num % 2 === 0);
console.log("every func output -", allEven);

// indexOf() returns the first index at which a given element can be found in the array, or -1 if it is not found.
console.log("\nindexOf func");
const index = number.indexOf(3);
console.log("indexOf func output -", index);

// includes() checks if an array contains a certain element, returning true or false.
console.log("\nincludes func");
const hasThree = number.includes(3);
console.log("includes func output -", hasThree);

// sort() sorts the elements of an array in place and returns the array.
console.log("\nsort func");
const sortedNumbers = number.sort((a, b) => a - b);
console.log("sort func output -", sortedNumbers);

// reverse() reverses the order of elements in the array in place.
console.log("\nreversed func");
const reversed = number.reverse();
console.log("reverse func output -", reversed);

// join() joins all elements of an array into a string, with an optional separator.
console.log("\n join func");
const joined = number.join("-");
console.log("joined func output -", joined);
