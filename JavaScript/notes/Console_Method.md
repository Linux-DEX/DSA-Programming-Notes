# console.log()
+ A built-in function that *allow you to output messages or values to the console*.

## Syntax
```js
console.log(msg1, msg2,..., msgN)
```

> [!NOTE]
>  *You can pass different messages (msg1, msg2, ...,msgN) by separating them with a comma as a parameter of the console.log() method*.

## Console.log() with client-sided javascript
+ Whenever we use the console.log() method in the frontend code, it print the output in the browser's console.

### Example
In the example below, *we have printed the "hello world!" message using the console.log() method*.
```js
<script>
console.log("hello world!");var num1 = 30;
var num2 = 20;
console.log("The sum of ", num1, " and ", num2, " is: ", num1 + num2);
</script>
```

+ *Output*
```txt
hello world!
The sum of 30 and 20 is: 50
```

## Console.log() with server-side javascript
The console.log() method with *the backend code prints the output in the terminal where the backend server is running*.

### Example
We have written the *below code printing the "hello world!" message into the app.js file*.
```js
let message = "hello world!";
console.log(message);
```

+ *Output*
```js
hello world!
```
