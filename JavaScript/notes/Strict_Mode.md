# Strict Mode
+ The purpose behind introducing the ~strict mode~ is to make the javascript code more secure.
+ The '**use strict**' literal expression is used to add the strict mode in the javascript code.
+ It removes the silent errors from the code, such as you can't use the variable without declaration, you can't modify the readable property of the object, etc.

## Enabling Strict Mode
To enable strict mode, you should write the following literal expression to the top of you code:

```js
'use strict';
```

## Strict Mode in the Global Scope

```js
"use strict";
let y = 50; // this is valid
x = 100;  // this is not valid
```

## Strict Mode in the Local Scope
You can also use the "strict mode" inside the particular function. So it will be applied only in the function scope.

```js
x = 100; // This is valid
document.write("The value of the X is - " + x);
function test() {
	"use strict";
	y = 50; // This is not valid
	document.write("The value of the y is: " + x);
}
test();
```

## Mistakes that you should't make in the strict mode
1. **You can't initialize the variable with a value without declaring it.**
```js
'use strict';
num = 10.99; // this is invalid
```

2. **Similarly, you can't use the object without declaring it.**
```js
'use strict';
numObj = { a:89, b: 10.23 }; // this is invalid
```

3. **You can't delete objects using the delete keyword.**
```js
'use strict';
let women = { name: "Linux-DEX", age: 23 };
delete woman; // this is invalid
```

4. **You can't delete the object prototype in the strict mode.**
```js
'use strict';
let women = { name: "Linux-DEX", age: 23 }
delete women.prototype; // this is invalid
```

5. **Deleting the function using the delete operator is not allowed.**
```js
'use strict';
function func() {}
delete func; // this is invalid
```

6. **You can't have a function with duplication parameter values.**
```js
'use strict';
function func(param1, param1, param2) {
	// function with 2 param1 is not allowed!
}
```

7. **You can't assign octal numbers to variables.**
```js
'use strict';
let octal = 010; // throws an error
```

8. **You can't use escape characters.**
```js
'use strict';
let octal = \010;  // throws an error
```

9. **You can't use reserved keywords like eval, arguments, public, etc., as an identifier.**
```js
'use strict';
let public = 100; // throws an error
```

10. **You can't write to the readable property of the object.**
```js
'use strict';
let person = {};

Object.defineProperty(person,'name', { value: "abc", writable: false });
obj1.name = "javascript"; // throws an error
```

11. **You can't assign values to the getters function.**
```js
'use strict';
let person = { get name() { return "javascript"; } };
obj1.name = "javascript"; // throws an error
```

12. **In the strict mode,when you use the "this" keyword inside the function, it refers to the reference object through which the function is invoked. if the refrence object is not specified, it refers to the undefined value.**
```js
'use strict';
function test() {
	console.log(this); // undefined
}
test();
```

13. **You can't use the "with" statement in the strict mode.**
```js
'use strict';
with (Math) { x = sin(2) }; // this will throw an error
```

14. **You can't use the eval() function to declare the variables for the security reason.**
```js
'use strict';
eval( "a = 8" )
```

15. **You can't use the keywords as an identifier that are reserved for the future. Bellow keywords are reserved for the future.**
    - Implements
    - Interface
    - package
    - private
    - protected
