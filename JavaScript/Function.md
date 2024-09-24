# Functions
A function is a reusable block of code or programming statements designed to perform a certain task. A function is declared by a function keyword followed by a name, followed by parentheses `()`. A parentheses can take a parameter. If a function take a parameter it will be called with argument. A function can also take a default parameter. To store a data to a function, a function has to return certain data types. To get the value we call or invoke a function. Function makes code:
+ Clean and easy to read
+ reusable
+ easy to test

A function can be declared or created in couple of ways:
+ *Declaration function*
+ *Expression function*
+ *Anonymous function*
+ *Arrow function*

## Function Declaration
Let us see how to declare a function and how to call a function.
```js
function functionName () {
	// code goes here
}
```

## Function without a parameter and return
Function can be declared without a parameter.

### Example
```js
function square () {
	let num = 2
	let sq = num * num
	console.log(sq)
}

square()
```

## Function returning value
Function can also return values, if a function does not return values the value of the function is undefined. Let us write the above functions with return. From now no, we return value to a function instead of printing it.

```js
function printFullName () {
	let firstName = "Linux"
	let lastName = "DEX"
	let space = " "
	let fullName = firstName + space + lastName
	return fullName
}

console.log(printFullName())
```

## Function with a parameter
In a function we can pass different data types(number, string, boolean, object, function) as a parameter.

```js
function areaOfCircle (r) {
	let area = Math.PI * r * r
	return area
}

console.log(areaOfCircle(10))
```

## Function with two parameters

### Syntax
```js
function functionName ( parm1,parm2 ) {
	// code goes here
}

functionName ( parm1, parm2 )
```

### Example
```js
function sumTwoNumbers ( numOne, numTwo ) {
	let sum = numOne + numTwo
	return sum
}

sumTwoNumbers(10, 20)
```

## Function with many parameters

### Syntax
```js
function functionName ( parm1, parm2, parm3, ...) {
	// code goes here
}

functionName ( parm1, parm2, parm3,...)
```

### Example 
```js
function sumArrayValues( arr ) {
	let sum = 0;
	for ( let i = 0 ; i < arr.length ; i++ ) {
		sum = sum + arr[i];
	}
	return sum;
}

const number = [1, 2, 3, 4, 5]
console.log(sumArrayValues(numbers))
```

## Function with unlimited number of parameters
Sometimes we do not know how many arguments the user going to pass. Therefore, we should know how to write a function which can take unlimited number of arguments. The way we do it has a significant difference between a function declaration(regular function) and arrow function. Let us see examples both in function declaration and arrow function.

### Unlimited number of parameters in regular function
A function declaration provides a function scoped arguments array like object. Any thing we passed as argument in the function can be accessed from arguments object inside the functions. 
```js
function sumAllNums () {
	console.log(arguments)
}

sumAllNums(1,2,3,4)
```

### Unlimited number of parameter in arrow function
Arrow function does not have the function scoped arguments object. To implement a function which takes unlimited number of arguments in an arrow function we use spread operator followed by any parameter name. Any thing we passed as argument in the function can be accessed as array in the arrow function. 
```js
const sumAllNums = (...args) => {
	// instead we use a parameter followed by spread operator (...)
	console.log(args)
}

sumAllNums(1,2,3,4)
```

## Anonymous Function
Anonymous function or without name
```js
const anonymousFun = function () {
	console.log(
		'I am an anonymous function and my value is stored in anonymousfun'
	)
}
```

## Expression Function
Expression functions are anonymous functions. After we create a function without a name and we assign it to a variable. To return a value from the function we should call the variable. 
```js
const square = function(n) {
	return n * n
}

console.log(square(2))
```

## Self Invoking Function
Self invoking functions are anonymous functions which do not need to be called to return a value.
```js
(function(n) {
	console.log(n * n)
})(2)
  
let squaredNum = (function(n) {
  return n * n
})(10)

console.log(squaredNum)
```

## Arrow Function
+ Arrow function is an alternative to write a function, however function declaration and arrow function have some minor differences.
+ Arrow function uses arrow instead of the keyword *function* to declare a function. Let us see both function declaration and arrow function.
```js
const square = n => {
	return n * n
}

console.log(square(2))

const printFullName = (firstName, lastName) => {
  return `${firstName} ${lastName}`
}

console.log(printFullName('Asabeneh', 'Yetayeh'))

const square = n => n * n
```

## Function with default parameters
Sometimes we pass default values of parameters, when we invoke the function if we do not pass an argument the default value will be used. Both function declaration and arrow function can have a default value or values.

### Syntax
```js
function functionName ( param = value ) {
	// codes
}

functionName()
functionName(arg)
```

### Example
```js
function greetings(name = 'Peter') {
  let message = `${name}, welcome to 30 Days Of JavaScript!`
  return message
}

console.log(greetings())
console.log(greetings('Asabeneh'))
```

## Nested Function
You can define the function inside the function, and the inner function is called the nested function.
```js
function outer() {
	console.log("outer function!!")
	function inner() {
		console.log("inner function!!")
	}
	inner()
}
outer()
```

## Special Function

### bind()
The bind() method creates a new function that, when called, has its this keyword set to the provided value, with a given sequence of arguments preceding any provided when the new function is called Function.prototype.bind()
```js
var module = {
  x: 42,
  getX: function() {
    return this.x;
  }
}

var unboundGetX = module.getX;
console.log(unboundGetX()); // The function gets invoked at the global scope
// expected output: undefined

var boundGetX = unboundGetX.bind(module);
console.log(boundGetX());
// expected output: 42
```

### call()
The call() method calls a function which given this value and arguments provided individually
```js
function Product(name, price) {
  this.name = name;
  this.price = price;
}

function Food(name, price) {
  Product.call(this, name, price);
  this.category = 'food';
}

console.log(new Food('cheese', 5).name);
// expected output: "cheese"
```

### apply()
The apply() method calls a function with a given this value, and arguments provided as an array (or an array-like object).
```js
var numbers = [5, 6, 2, 3, 7];

var max = Math.max.apply(null, numbers);

console.log(max);
// expected output: 7

var min = Math.min.apply(null, numbers);

console.log(min);
// expected output: 2
```


















