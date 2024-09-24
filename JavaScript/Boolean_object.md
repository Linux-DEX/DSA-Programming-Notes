# The Boolean Object
The JavaScript **Boolean** object represents two values, either "true" or "false". You can create a boolean object using the Boolean() constructor with a 'new' keyword. It takes a value as parameter and returns a boolean object. If value parameter is omitted or is 0, -0, null, false, NaN, undefined, or the empty string (""), the object has an initial value of false. In programming, the if-else statement evaluates either the code of the 'if' block or the 'else' block based on the boolean value of the conditional expression.

## Syntax
```js
const val = new Boolean(value);   
```
+ *It returns an object containing the boolean value.*

> [!NOTE]
> *you can create a boolean primitive in javascript by assigning a boolean value to a varaible*
> ```js
> let bool = true
> ```

## Boolean Properties

| Property    | Description                                                                   |
| ----------- | ----------------------------------------------------------------------------- |
| constructor | Returns a reference to the Boolean function that created the object.          |
| prototype   | The prototype property allows you to add properties and methods to an object. |

## Boolean Methods

| Method     | Description                                                                                                           |
| ---------- | --------------------------------------------------------------------------------------------------------------------- |
| toSource() | Returns a string containing the source of the Boolean object; you can use this string to create an equivalent object. |
| toString() | Returns a string of either "true" or "false" depending upon the value of the object.                                  |
| valueOf()  | Returns the primitive value of the Boolean object.                                                                    | 

## Example

```js
const boolObj = new Boolean('true')
typeof(boolObj)

// output
object
```

## Boolean() Function
The Boolean() function allows the developer to get the boolean value after evaluating the particular expression passed as a parameter.
```js
Boolean(Expression);
```
*Here value is an expression to evaluate and get related boolean values. The Boolean() function returns the true or false based on the expression passed as a parameter.*

### Example
```js
let res = Boolean( 100 > 90 );
console.log(res)

// output
true
```

## Javascript Falsy Boolean Values
The Boolean() function returns for the fasly values. There are six falsy values -false, null, undefined, 0 (zero), "" (empty string), NaN.

### Example
```js
Boolean(0)    // false
Boolean(-0)   // false
Boolean(null)  // false
Boolean(undefined)  // false
Boolean("")    // false
Boolean(NaN)   // false
Boolean(false)  // false
```

> [!NOTE]
> *All other values are truthy, and the Boolean() Function return true.*

### Example
```js
Boolean(1)   // true
Boolean(-1)   // true
Boolean("Hello")   //true
Boolean(true)   // true
Boolean(10.99)   // true
Boolean({name: "Linux"})   // true
Boolean(() => {return 1;})   // true
```













