
# Type Conversions
**Type Conversions** in javascript refers to the automatic or explicit process of converting data from one data type to another in javascript.

**There are two types of type convertion in javascript**:
- **Implicit** type convertion
- **Explicit** type convertion

## Implicit Type Conversion
+ When type conversion is done by javascript automatically, it is called **implicit type** conversion.
+ For example, when we use '+' operator with the **string** and **number** operands, javascript converts the **number** to a **string** and concatenates it with the string.

### Converting to String(Implicit conversion)
We used the `+` operator to implicitly convert different values to the string data type.

```js
"100" + 24;  // converts 24 to string
'100' + false  // converts false boolean value to string
"100" + null  // converts null keyword to string
```

> [!NOTE]
>  *Please note that to convert a value to string using `+` operator, one operand should be string.*

### Converting to Number(implicit conversion)
When you use the string values containing the digits with the arithmetic operators except for the `+` operator, it converts operands to numbers automatically and performs the arithemetic operation.

```js
'100' / 50; // converts '100' to 100
'100' - '50'; // convert '100' and '50' to 100 and 50
'100' * true; // convert true to 1
'100' - false;  // convert false to 0
'tp' / 50   // converts 'tp' to NaN
```

### Converting to Boolean(Implicit conversion)
When you use the Nullish (!!) operator with any variable, it Implicitly converts its value to the **boolean** value.

```js
num = !!0; // !0 = true, !!0 = false
num = !!1; // !1 = false , !!1 = true
str = !!"" // !"" = true, !!"" = false
str = !!"Hello"; // !"Hello" = false, !!"Hello" = true
```

### Null to Number(Implicit conversion)
In js, the **null** represents the empty. So, **null** automatically gets converted to **0** when we use it as an operand of the arithmetic operator.

```js
let num = 100 + null; // converts null to 0
num = 100 * null; // converts null to 0
```

### Undefined with Number and Boolean(Implicit conversion)
Using the **undefined** with the 'number' or 'boolean' value always gives the **NaN** in the output. Here, NaN means not a number.

```js
let num = 100 + undefined; // Prints NaN
```

## Explicit Type Conversion
In javascript, you can use the **constructor** functions or **built-in** functions to convert the type of the  variable.

### Converting to String(Explicit conversion)
You can use the **String()** constructor to convert the numbers, boolean, or other data types into the string.

```js
String(100); // number to string
String(null); // null to string
String(true); // boolean to string
```

> [!NOTE]
> - You can also use **typeof** operator to check the type of the resultant value.
> - We can also use the **toString()** method of number object to convert number to string.
```js
const num = 100;
num.toString() // convert 100 to '100'
```


### Converting to Number(Explicit conversion)
You can use the **Number()** constructor to convert a string into a number. We can also use **unary plus (+)** operator to convert a string to number.

```js
Number('100'); // converts '100' to 100
Number(false); // converts false to 0
Number(null); // converts null to 0
num = +"200"; // using the unary operator
```

| method / Operator | Description                                          |
| ----------------- | ---------------------------------------------------- |
| parseFloat()      | To extract the floating point number from the string |
| parseInt()        | To extract the integer from the string.              |
| +                 | It is an unary operator.                             |

### Converting to Boolean(Explicit Conversion)
You can use the **Boolean()** constructor to convert the other data types into boolean.

```js
Boolean(100); // Converts number to boolean (true)
Boolean(0); // 0 is falsy value (false)
Boolean(""); // Empty string is falsy value (false)
Boolean("Hi"); // Converts string to boolean (true)
Boolean(null); // null is falsy value (false)
```

> [!NOTE]
>  *You can use the Boolean() constructor to convert values to the boolean. All false value like 0, empty string, null, undefined, etc.., get converted to **false** and other value are converted to **true**.*


### Converting Date to String/Number
You can use Date object's Number() constructor or **getTimer()** method to convert the date string into the number.

```js
Number(date);
OR
date.getTime();
```

You can use the **String()** constructor or the **toString()** method to convert the date into a string.

```js
String(date);
OR
date.toString();
```
