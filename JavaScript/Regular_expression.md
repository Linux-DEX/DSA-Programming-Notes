# Regular Expressions and RegExp Object
A **Regular expression** (RegExp) in javascript is an object that describle a pattern of characters. It can contain the *alphabetical, numeric, and special characters.* Also, the regular expression pattern can have single or multiple characters.

The JavaScript **RegExp** class represents regular expressions, and both String and **RegExp** define methods that use regular expressions to perform powerful pattern-matching and search-and-replace functions on text.

The regular expression is used to search for the particular pattern in the string or replace the pattern with a new string.

There are two ways to construct the regular expression in javascript:
+ Using the RegExp() constructor.
+ Using the regular expression literal.

A regular expression could be defined with the **RegExp()** constructor, as follows -
```js
var pattern = new RegExp(pattern, attributes);

or

var pattern = /pattern/attributes;
```

## Modifiers

| Modifier | Description                                                                                                                                                           |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| i        | Perform case-insensitive matching.                                                                                                                                    |
| m        | Specifies that if the string has newline or carriage return characters, the ^ and $ operators will now match against a newline boundary, instead of a string boundary |
| g        | Perform a global match that is, find all matches rather than stopping after the first match.                                                                          |

## Brackets

| Expression | Description                                                            |
| ---------- | ---------------------------------------------------------------------- |
| [...]      | Any one character between the brackets.                                |
| \[^...]    | Any one character not between the brackets.                            |
| [0-9]      | It matches any decimal digit from 0 through 9.                         |
| [a-z]      | It matches any character from lowercase **a** through lowercase **z**. |
| [A-Z]      | It matches any character from uppercase **A** through uppercase **Z**. |
| [a-Z]      | It matches any character from lowercase **a** through uppercase **Z**. |

## Quantifiers

| Expression | Description                                                       |
| ---------- | ----------------------------------------------------------------- |
| p+         | It matches any string containing one or more p's.                 |
| p*         | It matches any string containing zero or more p's.                |
| p?         | It matches any string containing at more one p.                   |
| p{N}       | It matches any string containing a sequence of **N** p's.         |
| p{2,3}     | It matches any string containing a sequences of two or three p's. |
| p{2, }     | It matches any string containing a sequences of at least two p's. |
| p$         | It matches any string with p at the end of it.                    |
| ^p         | It matches any string with p at the beginning of it.              |
| ?!p        | It matches any string with is not followed by a string p.         |


| Expression       | Description                                                                                          |
| ---------------- | ---------------------------------------------------------------------------------------------------- |
| \[^a-zA-Z]       | It matches any string not containing any of the characters ranging from a through z and A through Z. |
| p.p              | It matches any string containing p, following by any character, in turn followed by another p.       |
| ^.{2}$           | It matches any string containing exactly two characters.                                             |
| < b >(.\*)</ b > | It matches any string enclosed within < b > and </ b >.                                              |
| p(hp)\*          | It matches any string containing a **p** followed by zero or more instances of the sequence **hp**.  |

## Literal characters

| Character    | Description                                                                                           |
| ------------ | ----------------------------------------------------------------------------------------------------- |
| Alphanumeric | Itself                                                                                                |
| \\0          | The NUL character (\u0000)                                                                            |
| \t           | Tab (\u0009                                                                                           |
| \n           | NewLine (\u000A)                                                                                      |
| \v           | Vertical tab (\u000B)                                                                                 |
| \f           | Form feed (\u000C)                                                                                    |
| \r           | Carriage return (\u000D)                                                                              |
| \xnn         | The Latin character specified by the hexadecimal number nn; for example, \x0A is the same as \n       |
| \uxxxx       | The Unicode character specified by the hexadecimal number xxxx; for example, \u0009 is the same as \t |
| \cX          | The control character ^X; for example, \cJ is equivalent to the newline character \n                  |

## Metacharacters

| Character       | Description                                       |
| --------------- | ------------------------------------------------- |
| .               | a single character                                |
| \s              | a whitespace character (space, tab, newline)      |
| \S              | non-whitespace character                          |
| \d              | a digit (0-9)                                     |
| \D              | a non-digit                                       |
| \w              | a word character (a-z, A-Z, 0-9, \_)              |
| \W              | a non-word character                              |
| [\b]            | a literal backspace (special case).               |
| [aeiou]         | matches a single character in the given set.      |
| \[^aeiou]       | matches a single character outside the given set. |
| (foo\|bar\|baz) | matches any of the alternatives specified.        |



