# Variable
+ A **JavaScript Variable** is simply a name of storage location. There are two types of variables in JavaScript: `local variable & global variable`.

## There are some rules while declaring a javascript variable.
1. Name must start with a letter (`a to z or A to Z`), underscore(`_`), or dollar(`$`) sign.
2. After first letter we can use digits(`0 to 9`), for example value1.
3. JavaScript variables are case sensitive, for example x and X are different variables.

## You can declare the variable in 4 ways
+ Without using any keywords.
+ Using the 'var' keyword.
+ Using the 'let' keyword.
+ Using the 'const' keyword.

# Variable Declaration in JavaScript
+ **Declare the variables without using any keywords.**
```js
<script>
	Money = 10;
	Name = "StringValue";
</script>
```

+ **Declare the variables using the var keyword.**
```js
<script>
	var money;
	var name;
	var firstName, lastName;
</script>
```

# Variable Initialization using the Assignment Operator
+ Storing a value in a variable is called **variable initialization**.
+ You can do variable initialization at the time of variable creation or at a later point in time when you need that variable.

```js
<script>
	var name = "Linux-DEX";
	var money;
	money = 2000.50;
</script>
```

# JavaScript Variable Scope
The scope of variable is the region of your program in which it is defined javascript variable have only two scopes.

## Global Variables
A global variable have global scope which means it can be defined anywhere in your javascript code.

```js
<script>
function abc()
{
	var x=10;//local variable
}
</script>
```

## Local Variables
A local variable will be visible only within a function where it is defined. Function parameters are always local to that function.

```js
<script>
var data=200;//gloabal variable
function a()
{
	document.writeln(data);
}
function b()
{
	document.writeln(data);
}
a();//calling JavaScript function
b();
</script>
```
