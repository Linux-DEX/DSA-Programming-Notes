# The String Object
The **String** object in javascript lets you work with a series of characters; it wraps javascript's string primitive data type with a number of helper methods.

As javascript automatically converts between string primitive and string objects, you can call any of the helper methods of the string object on a string primitive.

The String is a sequence of characters containing 0 or more characters. For example, "Hello" is a string.

JavaScript strings can be created as objects using the `String()` constructor or as primitives using string literals.

## Syntax
```js
const val = new String(value);    
```

We can create string primitives using string literals and the **String()** function as follows:
```js
str1 = 'hello world!!'  // using single quote
str2 = "Hello World!"; // using double quote 
str3 = 'Hello World'; // using back ticks 
str4 = String('Hello World!'); // using String() function
```

## String Properties

| Property    | Description                                                                   |
| ----------- | ----------------------------------------------------------------------------- |
| constructor | Returns a reference to the string function that created the object.           |
| length      | Returns the length of the string.                                             |
| prototype   | The prototype property allows you to add properties and methods to an object. |

## String Methods

| Property        | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| fromCharCode()  | Converts the sequence of UTF-16 code units into the string. |
| fromCodePoint() | Creates a string from the given sequence of ASCII values.   |

| Method              | Description                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| at()                | Returns the character from the specified index.                                                                                |
| charAt()            | Returns the character at the specified index.                                                                                  |
| charCodeAt()        | Returns a number indicating the Unicode value of the character at the given index.                                             |
| codePointAt()       | Returns a number indicating the Unicode value of the character at the given index.                                             |
| concat()            | Combines the text of two strings and returns a new string.                                                                     |
| endsWith()          | Checks whether the string ends with a specific character or substring.                                                         |
| includes()          | To check whether one string exists in another string.                                                                          |
| indexOf()           | Returns the index within the calling String object of the first occurrence of the specified value, or -1 if not found.         |
| lastIndexOf()       | Returns the index within the calling String object of the last occurrence of the specified value, or -1 if not found.          |
| localeCompare()     | Returns a number indicating whether a reference string comes before or after or is the same as the given string in sort order. |
| match()             | Used to match a regular expression against a string.                                                                           |
| matchAll()          | Used to match all occurrences of regular expression patterns in the string.                                                    |
| normalize()         | To get the Unicode normalization of the string.                                                                                |
| padEnd()            | To add padding to the current string with different strings at the end.                                                        |
| padStart()          | To add padding to the current string with different strings at the start.                                                      |
| replace()           | Used to find a match between a regular expression and a string and replace the matched substring with a new one.               |
| replaceAll()        | Used to find a match between a regular expression and a string and replace all the matched substring with a new one.           |
| repeat()            | To get a new string containing the N number of copies of the current string.                                                   |
| search()            | Executes the search for a match between a regular expression and a specified string.                                           |
| slice()             | Extracts a section of a string and returns a new string.                                                                       |
| split()             | Splits a String object into an array of strings by separating the string into substrings.                                      |
| substr()            | Returns the characters in a string beginning at the specified location through the specified number of characters.             |
| substring()         | Returns the characters in a string between two indexes into the string.                                                        |
| toLocaleLowerCase() | The characters within a string are converted to lowercase while respecting the current locale.                                 |
| toLocaleUpperCase() | The characters within a string are converted to the upper case while respecting the current locale.                            |
| toLowerCase()       | Returns the calling string value converted to lowercase.                                                                       |
| toString()          | Returns a string representing the specified object.                                                                            |
| toUpperCase()       | Returns the calling string value converted to uppercase.                                                                       |
| trim()              | It removes white spaces from both ends.                                                                                        |
| trimEnd()           | It removes white spaces from the start.                                                                                        |
| trimStart()         | It removes white spaces from the end.                                                                                          |
| valueOf()           | Returns the primitive value of the specified object.                                                                           |

## Creating javascript string objects
```js
const str = new String("Hello World!")
console.log(typeof str)

// output
object
```

## Accessing a string
You can access the string characters using its index. The string index starts from 0.

```js
let str = "Linux-DEX"
console.log(str[0])
console.log(str[7])

// output
L
E
```

## Strings are Case-sensitive
In javascript, strings are case-sensitive. It means lowercase and uppercase characters are different.

```js
let char1 = 's'
let char2 = 'S'
let ans = char1 == char2
console.log(ans)

// output
false
```

## Strings are Immutable
In javascript, you can't change the characters of the string. However, you can update the whole string.
```js
let str = "Linux"
str[0] = "U"
console.log(str)
str = "DEX"
console.log(str)

// output
Linux
DEX
```

## Escape character

| Escape Character | Description     |
| ---------------- | --------------- |
| \\"              | Double quote    |
| \\'              | Single quote    |
| \\\\             | Backslash       |
| \\n              | New line        |
| \\t              | Tab             |
| \\b              | backSpace       |
| \\f              | Form feed       |
| \\v              | Vertical tab    |
| \\r              | Carriage return |
| \\uXXXX          | unicode escape  |

### Example
```js
let str1 = "Your\'s Welcome!!"
let str2 = "Backslash \\"
console.log(str1)
console.log(str2)

// output
Your's Welcome!
Backslash \
```

## String HTML Wrappers

| Method      | Description                                                                                           |
| ----------- | ----------------------------------------------------------------------------------------------------- |
| anchor()    | Creates an HTML anchor that is used as a hypertext target.                                            |
| big()       | Creates a string to be displayed in a big font as if it were in a < big > tag.                        |
| blink()     | Creates a string to blink as if it were in a < blink > tag.                                           |
| fixed()     | Causes a string to be displayed in fixed-pitch font as if it were in a < tt > tag                     |
| bold()      | Creates a string to be displayed as bold as if it were in a < b > tag.                                |
| fontcolor() | Causes a string to be displayed in the specified color as if it were in a < font color="color" > tag. |
| italics()   | Causes a string to be italic, as if it were in an < i > tag.                                          |
| link()      | Creates an HTML hypertext link that requests another URL.                                             |
| small()     | Causes a string to be displayed in a small font, as if it were in a < small > tag.                    |
| strike()    | Causes a string to be displayed as struck-out text, as if it were in a < strike > tag.                |
| sub()       | Causes a string to be displayed as a subscript, as if it were in a < sub > tag                        |
| sup()       | Causes a string to be displayed as a superscript, as if it were in a < sup > tag                      |













