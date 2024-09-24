# Control Flow

Control flow is **the order in which the computer executes statements in a script.** Code is run in order from the first line in the file to the last line, unless the computer run across the (*extremely frequent*) structures that change the control flow, such as conditionals and loops.

# Conditionals 

Conditional statements are used for make decisions based on different conditions. By default, statements in Javascript script executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two ways.

+ **Conditional execution:** a block of one or more statements will be executed if a certain expression is true.
+ **Repetitive execution:** a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover _if_, _else_ , _else if_ statements. The comparison and logical operators we learned in the previous sections will be useful in here.

Conditions can be implementing using the following ways:
+ if
+ if else
+ if else if else
+ switch
+ ternary operator

## If

In JavaScript and other programming languages the key word *if* is to used check if a condition is true and to execute the block code. To create an if condition, we need *if* keyword, condition inside a parenthesis and block of code inside a curly bracket `{ }`

### syntax
```js
if ( condition ) {
   // this part of code runs for truthy condition
}
```

### example
```js
let num = 3
if ( num > 0 ) {
	console.log(`${num} is a positive number`)
}
```
As you can see in the condition example above, 3 is greater than 0, so it is a positive number. The condition was true and the block of code was executed. However, if the condition is false, we won't see any results.

> [!NOTE]
> *The same goes for the second condition, if isRaining is false the if block will not be executed and we do not see any output. In order to see the result of a falsy condition, we should have another block, which is going to be _else_.*

## If Else
If condition is true the first block will be executed, if not the else condition will be executed.

### Syntax
```js
if ( condition ) {
	// this part of code runs for truthy condition
} else {
	// this part of code runs for falsy condition
}
```

### Example
```js
let num = 3
if ( num > 0 ) {
	console.log(`${num} is positive number`)
} else {
	console.log(`${num} is negative number`)
}
```
The last condition is false, therefore the else block was executed. What if we have more than two conditions? In that case, we would use *else if* conditions.

## If Else if Else
On our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions instead we make decisions based on multiple conditions. As similar to our daily life, programming is also full of conditions. We use *else if* when we have multiple conditions.

### Syntax
```js
if ( condition ) {
	// code
} else if ( condition ) {
	// code
} else {
	// code
}
```

### Example
```js
let a = 0
if (a > 0) {
	console.log(`${a} is a positive number`)
} else if (a < 0) {
	console.log(`${a} is a negative number`)
} else if (a == 0) {
	console.log(`${a} is zero`)
} else {
	console.log(`${a} is not a number`)
}
```

## Switch
Switch is an alternative for **if else if else else**. The switch statement starts with a *switch* keyword followed by a parenthesis and code block. Inside the code block we will have different cases. Case block runs if the value in the switch statement parenthesis matches with the case value. The break statement is to terminate execution so the code execution does not go down after the condition is satisfied. The default block runs if all the cases don't satisfy the condition.

### Syntax
```js
switch(caseValue){
	case 1:
		// code
		break
	case 2:
		// code
		break
	case 3:
		// code
		break
	default:
		// code
}
```

### Example
```js
let weather = 'cloudy'
switch (weather) {
  case 'rainy':
    console.log('You need a rain coat.')
    break
  case 'cloudy':
    console.log('It might be cold, you need a jacket.')
    break
  case 'sunny':
    console.log('Go out freely.')
    break
  default:
    console.log(' No need for rain coat.')
}
```

## Ternary operators
Another way to write conditional is using ternary operators. 
```js
let isRaining = true
isRaining
 ? console.log("You need a rain coat.")
 : console.log("No need for a rain coat.")
```

# Loops
In programming language to carry out repetitive task we use different kinds of loops. The following example are the commonly used loops in javascript and other programming language.

## For Loop
The javascript **for** loop is used to execute a block of cod repetatedly, until a specified condition evaluates to false.

It includes the following three important parts
+ **Initialization:** The loop initialization expression is where we initialize our counter to a starting value. The initialization statement is executed before the loop begins.
+ **Condition:** The condition expression which will test if a given condition is true or not. If the condition is true, then the code given inside the loop will be executed. Otherwise, the control will come out of the loop.
+ **Iteration:** The iteration expression is where you can increase or decrease your counter.

### Syntax
```js
for ( initialization; condition; iteration ) {
	// code goes here
}
```

### Example
```js
for ( let i = 0; i <= 5; i++ ){
	console.log(i)
}
```

## For...in Loop
+ The **for...in** loop in javascript is used to loop through an object's properties. The javascript **for...in** loop is a variant of the for loop. 
+ The **for** loop can't be used to traverse through the object properties. So, the **for...in** loop is introduced to traverse through all object properties.
+ The **for...in** loop in javascript can also be used to iterate through the elements of an array.

### Syntax
```js
for ( variableName in object ) {
	// code goes here
}
```

### Example
```js
let car = {
brand: "OD",
model: "Q7",
color: "Black"
}
for ( key in car ) {
	console.log(`${key} => ${car[key]}`)
}
```

## For...of Loop
+ The **for...of** loop in javascript is used to traverse elements of the iterable object. In each iteration, it gives an element of the iterable object. Iterable include array, string, maps, sets, and generators.
+ The javascript **for...of** loop is an much more efficient way to iterate over iterables than using a **for...in** loop.
+ The **for...of** loop iterates over the property value while the for...in loop is used to iterate through the keys (*property name*) of an object.

### Syntax
```js
for ( const element of iterable ) { 
	// code come here
}
```

### Example
```js
const number = [1, 2, 3, 4, 5]
for ( const num of numbers ) {
	console.log(num)
}
```

## While loop
A **while** statement in JavaScript creates a loop that executes a block of code repeatedly, as long as the specified condition is **true**. The condition is evaluated before the execution of the block of code.

### Syntax
```js
while ( expression ) {
	// code come here
}
```

### Example
```js
let i = 0
while ( i <= 5 ) {
	console.log(i)
	i++
}
```

## do...while Loop
The **do...while** loop is similar to the **while** loop except that the condition check happens at the end of the loop. This means that the loop will always be executed at least once, even if the condition is **false**.

### Syntax
```js
do {
	// code come here
} while ( expression )
```

# Loop Control 
JavaScript provides full control to handle loops and switch statements. There may be a situation when you need to come out of a loop without reaching its bottom. There may also be a situation when you want to skip a part of your code block and start the next iteration of the loop.

| keyword  | Explanation                                                                                                                                                                                                            |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| break    | The 'break' keyword is used to come out of the loop.                                                                                                                                                                   |
| continue | The 'continue' keyword is used to skip the current iteration of the loop.                                                                                                                                              |
| label    | The 'label' is not a keyword, but you can use any identifier followed by a colon (:) to give a label to the loop. After that, you can use the label to target the particular loop with the break and continue keyword. |

## break statement
The JavaScript **break** statement, which was briefly introduced with the _switch_ statement, is used to exit a loop early, breaking out of the enclosing curly braces.

### Example
```js
for ( let i = 0; i <= 5; i++ ) {
	if ( i == 3 ){
		break
	}
	console.log(i)
}
```

## continue statement
The JavaScript **continue** statement tells the interpreter to immediately start the next iteration of the loop and skip the remaining code block. When a **continue** statement is encountered, the program flow moves to the loop check expression immediately and if the condition remains true, then it starts the next iteration, otherwise the control comes out of the loop.

### Example
```js
for ( let i = 0 ; i <= 5 ; i++ ) {
	if ( i == 3 ) {
		continue
	}
	console.log(i)
}
```

## Labels 
Starting from JavaScript 1.2, a label can be used with **break** and **continue** to control the flow more precisely. A **label** is simply an identifier followed by a colon (:) that is applied to a statement or a block of code. We will see two different examples to understand how to use labels with break and continue.

### Example
```js
let sum = 0, a = 1
outerloop: while ( true ) {
	a = 1
	innerloop: while ( a < 3 ) {
		sum += a
		if ( sum > 12 ) {
			break outerloop
		}
		console.log("sum = " + sum ) 
		a++
	}
}
```

# User Defined Iterators
In javascript, an iterable is an object which has Symbol.iterator() method in the object prototype. Some examples of iterable are array, set, map, string, etc. The Symbol.iterator() method returns an object containing the next() method is called **iterator.** Here, the next() method returns the elements of iterable in each call.

## next() Method
The next() method of the iterator object returns an object containing two key-value pair given below.
+ **value:** The value key contains the element as a value.
+ **done:** The done key contains the boolean value. It contains true if all iterations of iterable are finished. Otherwise, it contains false.

### Example
```js
const myArray = [1, 2, 3];

const myIterator = {
	currentIndex: 0,
	next: function () {
		if ( this.currentIndex < myArray.length ) {
			return {
				value: myArray[this.currentIndex++],
				done: false
			};
		} else {
			return { done: true };
		}
	}
};

console.log(myIterator.next());
console.log(myIterator.next());
console.log(myIterator.next());
console.log(myIterator.next());
```







