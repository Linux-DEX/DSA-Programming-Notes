# Array
+ The JavaScript **Array** object lets you store multiple values in a single variable. 
+ An array is used to store a sequential collection of multiple elements of same or different data types. 
+ In JavaScript, arrays are dynamic, so you don’t need to specify the length of the array while defining the array. 
+ The size of a JavaScript array may decrease or increase after its creation.

## Syntax
```js
const arr = new Array(val1, val2, val3, ..., valN)
```

> [!NOTE]
> + **val1, val2, val3, ..., valN** - *It takes multiple values as an argument to initialize ana array with them.*

## Return value
It returns an array object.

> [!NOTE] 
>  When you pass the single numeric argument to the Array() constructor, it defines the array of argument length containing the undefined values. The maximum length allowed for an array is 4,294,967,295.

```js
const fruits = ["apple", "orange", "mango"]
fruits[0] --> apple
fruits[1] --> orange
fruits[2] --> mango
```

## Array Reference
In JavaScript, the Array object enables storing collection of multiple elements under a single variable name. It provides various methods and properties to perform operations on an array. 

| Name        | Description                                                        |
| ----------- | ------------------------------------------------------------------ |
| constructor | Returns a reference to the array function that created the object. |
| length      | Reflects the number of elements in an array.                       |

| Name      | Description                                               |
| --------- | --------------------------------------------------------- |
| from()    | Creates a shallow copy of the array                       |
| isArray() | Returns boolean values based on the argument is an array. |
| Of()      | Creates an array from multiple arguments.                 |

| Name             | Description                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------- |
| at()             | To get element from the particular index.                                                                               |
| concat()         | Returns a new array comprised of this array joined with another array (s) and/or value(s).                              |
| copyWithin()     | To Copy part of the array into the same array at different locations.                                                   |
| entries()        | To get each entry of the array.                                                                                         |
| every()          | Returns true if every element in this array satisfies the provided testing function.                                    |
| fill()           | To fill the array with static values.                                                                                   |
| filter()         | Creates a new array with all of the elements of this array for which the provided filtering function returns true.      |
| find()           | To find an element satisfying the condition.                                                                            |
| findIndex()      | To find an index of the element satisfying the condition.                                                               |
| findLast()       | To find an element satisfying the condition from the last.                                                              |
| flat()           | To flatten the array.                                                                                                   |
| flatMap()        | To get a new array after flattening the array.                                                                          |
| forEach()        | Calls a function for each element in the array.                                                                         |
| Includes()       | Returns a boolean value if the array contains the specific element.                                                     |
| indexOf()        | Returns the first (least) index of an element within the array equal to the specified value, or -1 if none is found.    |
| join()           | Joins all elements of an array into a string.                                                                           |
| Keys()           | Returns an array iterator containing the key for each array element.                                                    |
| lastIndexOf()    | Returns the last (greatest) index of an element within the array equal to the specified value, or -1 if none is found.  |
| map()            | Creates a new array with the results of calling a provided function on every element in this array.                     |
| pop()            | Removes the last element from an array and returns that element.                                                        |
| push()           | Adds one or more elements to the end of an array and returns the new length of the array.                               |
| reduce()         | Apply a function simultaneously against two values of the array (from left-to-right) as to reduce it to a single value. |
| reduceRight()    | Apply a function simultaneously against two values of the array (from right-to-left) as to reduce it to a single value. |
| reverse()        | Reverses the order of the elements of an array -- the first becomes the last, and the last becomes the first.           |
| shift()          | Removes the first element from an array and returns that element.                                                       |
| slice()          | Extracts a section of an array and returns a new array.                                                                 |
| some()           | Returns true if at least one element in this array satisfies the provided testing function.                             |
| toSorted()       | Sorts the elements of an array in a specific order.                                                                     |
| sort()           | Sorts the elements of an array.                                                                                         |
| splice()         | Adds and/or removes elements from an array.                                                                             |
| toLocaleString() | To convert array elements into the string.                                                                              |
| toReversed()     | Returns a reverse of the array.                                                                                         |
| toSpliced()      | This method returns a new array with some elements removed and/or replaced at a given index.                            |
| toString()       | Returns a string representing the array and its elements.                                                               |
| unshift()        | Adds one or more elements to the front of an array and returns the new length of the array.                             |
| values()         | To get an iterator containing values of each array index.                                                               |
| with()           | This method returns a new array with the element at the given index replaced with the given value.                      |

## Example

```js
let strs = new Array("Hello", "World!", "Linux-DEX")
console.log(strs)   // ['Hello','World!','Linux-DEX']

let cars = new Array(20)
console.log(cars)   // [ <20 empty items> ]
```

```js
const arr1 = [10, 40, 50, 20, 30]
const arr2 = ["Hello", "Hi", "How", "Why"]
const arr3 = [true, false, true, true]
```

> [!NOTE]
> *The array index starts from 0. So, you can access the array element using the index.*
> ```js
> let number = arr[index]
> ```


```js
const nums = [1, 5, 6, 8, 9]
console.log(nums[0])  // 1
console.log(nums[2])  // 6
```

> [!NOTE]
> *The length property of the array is used to find the length of  the array.*
> ```js
> let len = arr.length;
> ```

```js
const nums = [1, 5, 6, 8, 90]
console.log(nums.length)   // 5
```

