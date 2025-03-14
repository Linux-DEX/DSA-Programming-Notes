# Strings
Strings are texts, which are under **single, double, back-tick** quote.

## String Concatenation
Connecting two or more strings together is called concatenation.

```js
let firstName = "linux"
let lastName = "DEX"
let fullName = firstName + lastName;
```

## Concatenating Using Addition Operator
Concatenating using the addition operator is an old way. This way of concatenating is tedious and error-prone.

```js
// Declaring different variables of different data types
let space = ' '
let firstName = 'Asabeneh'
let lastName = 'Yetayeh'
let country = 'Finland'
let city = 'Helsinki'
let language = 'JavaScript'
let job = 'teacher'
let age = 250

let fullName =firstName + space + lastName
let personInfoOne = fullName + '. I am ' + age + '. I live in ' + country; // ES5 string addition
```

## Long Literal Strings
+ A string be a single character or paragraph or a page.
+ If the string length is too big it does not fit in one line. We can use backslash character(\\) at the end of each line to indicate that the string will continue on the next line.

```js
const paragraph = "My name is Asabeneh Yetayeh. I live in Finland, Helsinki.\
I am a teacher and I love teaching. I teach HTML, CSS, JavaScript, React, Redux, \
Node.js, Python, Data Analysis and D3.js for anyone who is interested to learn. \
In the end of 2019, I was thinking to expand my teaching and to reach \
to global audience and I started a Python challenge from November 20 - December 19.\
It was one of the most rewarding and inspiring experience.\
Now, we are in 2020. I am enjoying preparing the 30DaysOfJavaScript challenge and \
I hope you are enjoying too."
```


## Escape Sequences in Strings
In javascript and other programming languages `\` followed by some characters is an escape sequence.

| escape sequences | description         |
| ---------------- | ------------------- |
| \\n              | New  line           |
| \\t              | Tab, means 8 spaces |
| \\\\             | Back slash          |
| \\'              | Single quote(')     |
| \\"              | Double quote(")     |

## Template Literals (Template Strings)
We can inject data as expressions inside a template string. To inject data we enclose the expression with a curly bracket({}) preceded by a $ sign.

```js
`String literal text`
`String literal text ${expression}`
```

### Example
```js
let a = 2
let b = 3
console.log(`${a} is greater than ${b}: ${a > b}`)
```

# String Methods
+ Everything in javascript is an object.
+ *A string is a primitive data type that means we can not modify it once it is created.*

## length
The string length method returns the number of characters in a string included empty space.
### example
```js
let js = 'Javascript';
console.log(js.length) // 10
```

## Accessing characters in a string
We can access each character in a string using it index. In programming, counting starts from 0. The first index of the string is zero, and the last index is the length of the string minus one.

### Example
```js
let string = "Javascript";
let firstLetter = string[0];

console.log(firstLetter) // J
```

## toUpperCase()
This method changes the string to uppercase letters.

### Example
```js
let string = "javascript"
console.log(string.toUpperCase()) // JAVASCRIPT
```

## toLowerCase()
This method changes the string to lowercase letters.

### Example
```js
let string = "JavaScript";
console.log(string.toLowerCase()) // javascript
```

## substr()
It takes two arguments, the string index and number of characters to slice.

### Example
```js
let string = "Javascript";
console.log(string.substr(4,6)) // Script
```

## substring()
It takes two arguments, the starting index and the stopping index but it doesn't include the character at the stopping index.

### Example
```js
let string = "Javascript";
console.log(string.substring(0,4)) // Java
console.log(string.substring(4)) //  script
```

## split()
The split method splits a string at a specified place.

### Example
```js
let string = "javascript is asynchronous";
console.log(string.split(' '))  // split array -> ["javascript", "is", "asynchronous"]
```

## trim()
Remove trailing space in the beginning or the end of a string.

### Example
```js
let string = '   javascript is asynchronous   '

console.log(string)
console.log(string.trim(' ')) // javascript is asynchronous
```

## includes()
It takes a substring argument and it checks if substring argument exists in the string. *includes() returns a boolean*. If a substring exist in a string, it return true, otherwise it return false.

### Example
```js
let string = "Linux DEX javascript Notes";

console.log(string.includes("Linux"))  // true
console.log(string.includes("script")) // true
console.log(string.includes("JAVA"))   // false
```

## replace()
Takes as a parameter the old substring and a new substring.

### Syntax
```js
string.replace(oldsubstring, newsubstring)
```

### Example
```js
let string = "Linux DEX javascript Notes"
console.log(string.replace("javascript", "typescript")) // Linux DEX typescript NOtes
```

## charAt()
Takes index and it returns the value at that index.

### Syntax
```js
string.charAt(index)
```

### Example
```js
let string = "Linux DEX javascript Notes"
console.log(string.charAt(0))  // L
```

## charCodeAt()
Takes index and it returns char code (ASCII number) of the value at that index.

### Syntax
```js
string.charCodeAt(index)
```

### Example
```js
let string = "Linux DEX javascript Notes"
console.log(string.charCodeAt(6)) // D ASCII number is 68
```

## indexOf()
Takes a substring and if the substring exists in a string it returns the first position of the substring if does not exist it returns -1.

### Syntax
```js
string.indexOf(substring)
```

### Example
```js
let string = "Linux DEX javascript Notes"
console.log(string.indexOf("D")) // 6
```

## lastIndexOf()
Takes a substring and if the substring exists in a string it returns the last position of the substring if it does not exist it returns -1

### Syntax
```js
string.lastIndexOf(substring)
```

### Example
```js
let string = 'I love JavaScript. If you do not love JavaScript what else can you love.'

console.log(string.lastIndexOf('love'))       // 67
console.log(string.lastIndexOf('you'))        // 63
console.log(string.lastIndexOf('JavaScript')) // 38
```

## concat()
It takes many substrings and joins them.

### Syntax
```js
string.concat(substring, substring, substring)
```

### Example
```js
let string = "linux"
console.log(string.concat("Dex", "javascript", "Notes")) // linuxDexjavascriptNotes
```

## startsWith
It takes a substring as an argument and it checks if the string starts with that specified substring. It returns a boolean(true or false).

### Syntax
```js
string.startsWith(substring)
```

### Example
```js
let string = 'Love is the best to in this world'

console.log(string.startsWith('Love'))   // true
console.log(string.startsWith('love'))   // false
console.log(string.startsWith('world'))  // false
```

## endsWith
It takes a substring as a argument and it checks if the string ends with that specified substring. It returns a boolean(true or false).

### Syntax
```js
string.endsWith(substring)
```

### Example
```js
let string = 'Love is the most powerful feeling in the world'

console.log(string.endsWith('world'))         // true
console.log(string.endsWith('love'))          // false
console.log(string.endsWith('in the world')) // true
```

## search
It takes a substring as an arugment and it returns the index of the first match. The search value can be a string or a regular expression pattern.

### Syntax
```js
string.search(substring)
```

### Example
```js
let string = 'I love JavaScript. If you do not love JavaScript what else can you love.'
console.log(string.search('love'))          // 2
console.log(string.search(/javascript/gi))  // 7
```

## match
It takes a substring or regular expression pattern as an argument and it returns an array if there is match if not it return null. Let us see how a regular expression pattern looks like. It starts with *sign and ends with* sign.

### Syntax
```js
string.match(substring)
```

### Example
```js
let string = 'love'
let patternOne = /love/     // with out any flag
let patternTwo = /love/gi   // g-means to search in the whole text, i - case insensitive

let string = 'I love JavaScript. If you do not love JavaScript what else can you love.'
console.log(string.match('love'))
```

## repeat()
It takes a number as argument and it returns the repeated version of the string.

### Syntax
```js
string.repeat(n)
```

### Example
```js
let string = 'love'
console.log(string.repeat(10)) // lovelovelovelovelovelovelovelovelovelove
```



