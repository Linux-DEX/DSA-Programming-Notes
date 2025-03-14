# The Number Object
The javascript **Number** object represents numerical data as floating-point numbers.It contains different properties (constants) and methods for working on numbers. In general, you do not need to worry about **Number** object because the browser automatically converts number literals to instances of the number class.

A javascript Number object can be defined using the Number constructor. Other types of data such as strings, etc., can be converted to numbers using `Number()` function.

## Syntax
```js
const val = new Number(number);
```

## Number Properties

| Property          | Description                                                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| EPSILON           | It represents the difference between 1 and the smallest floating point number greater than 1.                                                         |
| MAX_SAFE_INTEGER  | It returns the maximum safe integer value.                                                                                                            |
| MAX_VALUE         | The largest possible value a number in JavaScript can have 1.7976931348623157E+308.                                                                   |
| MIN_SAFE_INTEGER  | It returns the minimum safe integer value.                                                                                                            |
| MIN_VALUE         | The smallest possible value a number in JavaScript can have 5E-324.                                                                                   |
| NaN               | Equal to a value that is not a number.                                                                                                                |
| NEGATIVE_INFINITY | A value that is less than MIN_VALUE.                                                                                                                  |
| POSITIVE_INFINITY | A value that is greater than MAX_VALUE.                                                                                                               |
| prototype         | A static property of the Number object. Use the prototype property to assign new properties and methods to the Number object in the current document. |
| constructor       | Returns the function that created this object's instance. By default this is the Number object.                                                       |

## Number Methods
The Number object contains only the default methods that are a part of every object's definition.

| Method           | Description                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------- |
| toExponential()  | Forces a number to display in exponential notation, even if the number is in the range of standard notation.  |
| toFixed()        | Formats a number with a specific number of digits to the right of the decimal.                                |
| toLocaleString() | Returns a string value version of the current number in a format that may vary according to local settings.   |
| toPrecision()    | Defines how many total digits (including digits to the left and right of the decimal) to display of a number. |
| toString()       | Returns the string representation of the number's value.                                                      |
| valueOf()        | Returns the number's value.                                                                                   |

| Method          | Description                                          |
| --------------- | ---------------------------------------------------- |
| isNaN()         | It check whether the value is a valid number or not  |
| isFinite()      | It check whether the number is finite.               |
| isInteger()     | Returns Boolean when the number is an integer value. |
| isSafeInteger() | It ensures that the integer is a safe integer.       |
| parseFloat()    | Parses the float value from the string.              |
| parseInt()      | Parses the integer value from the string.            |

### Example

```js
const num = new Number(20);
console.log(num)
console.log(typeof(num))

// output
20
object
```



















