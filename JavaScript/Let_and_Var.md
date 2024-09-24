# Let & Var
## Let keyword
+ The **let** statement is used to declare a local variable in Javascript.
+ It is similar to the **var** keyword, but /it has some restriction in scoping in comparison of the var keyword/.
+ The let keyword can enhance our code readability and decreases the change of programming error.
+ A variable declared with the **let keyword in limited to the** `block-scoped only`.

```js
let greeter = "Hey hi";
let times = 5;
if ( times > 3 )
{
	let hello = "Say Hello javascript";
	console.log(hello);
}
console.log(hello);
```

+ **output**:
```js
console.log(hello) // compile error: greeter is not defined
```

## Var keyword
+ The **var** statement is used to declare a variable in javascript.
+ A variable decalred with the **var keyword** is defined throughout the program.

```js
var greeter = "hey hi";
var times = 5;
if ( times > 3 )
{
        var greeter = "Say Hello javascript";
}
console.log(greeter)
```

+ **output**:
```js
Say Hello Javascript
```
