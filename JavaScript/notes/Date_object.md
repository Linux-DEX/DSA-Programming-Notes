# The Date Object
The Date object is a datatype built into the javascript language. Date object are created with the **new Date()** 

The ECMAScript standard required the Date object to be able to represent any date and time, to millisecond precision, within 100 million days before or after 1/1/1970.This is a range of plus or minus 273,785 years, so JavaScript can represent date and time till the year 275755.

## Syntax
```js
new Date( )
new Date(milliseconds)
new Date(datestring)
new Date(year, month, date[ ,hour, minute, second, millisecond ])
```

> [!NOTE]
> + **No Argument :** With no arguments, the Date() constructor creates a Date object set to the current date and time.
> + **milliseconds :** When one numeric argument is passed, it is taken as the internal numeric representation of the date in milliseconds, as returned by the getTime() method. For example, passing the argument 5000 creates a date that represents five seconds past midnight on 1/1/70.
> + **datestring :** When one string argument is passed, it is a string representation of a date, in the format accepted by the **Date.parse()** method.
> + **year :** Integer value representing the year. For compatibility (in order to avoid the Y2K problem), you should always specify the year in full; use 1998, rather than 98.
> + **month :** Integer value representing the month, beginning with 0 for January to 11 for December.
> + **date :** Integer value representing the day of the month.
> + **hour :** Integer value representing the hour of the day (24-hour scale).
> + **minute :** Integer value representing the minute segment of a time reading.
> + **second :** Integer value representing the second segment of a time reading.
> + **millisecond :** Integer value representing the millisecond segment of a time reading.

## Date Properties

| Property    | Description                                                                  |
| ----------- | ---------------------------------------------------------------------------- |
| constructor | Specifies the function that creates an object's prototype.                   |
| prototype   | The prototype property allows you to add properties and methods to an object |

## Date Methods

| Method               | Description                                                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Date()               | Returns today's date and time                                                                                          |
| getDate()            | Returns the day of the month for the specified date according to local time.                                           |
| getDay()             | Returns the day of the week for the specified date according to local time.                                            |
| getFullYear()        | Returns the year of the specified date according to local time.                                                        |
| getHours()           | Returns the hour in the specified date according to local time.                                                        |
| getMilliseconds()    | Returns the milliseconds in the specified date according to local time.                                                |
| getMinutes()         | Returns the minutes in the specified date according to local time.                                                     |
| getMonth()           | Returns the month in the specified date according to local time.                                                       |
| getSeconds()         | Returns the seconds in the specified date according to local time.                                                     |
| getTime()            | Returns the numeric value of the specified date as the number of milliseconds since January 1, 1970, 00:00:00 UTC.     |
| getTimezoneOffset()  | Returns the time-zone offset in minutes for the current locale.                                                        |
| getUTCDate()         | Returns the day (date) of the month in the specified date according to universal time.                                 |
| getUTCDay()          | Returns the day of the week in the specified date according to universal time.                                         |
| getUTCFullYear()     | Returns the year in the specified date according to universal time.                                                    |
| getUTCHours()        | Returns the hours in the specified date according to universal time.                                                   |
| getUTCMilliseconds() | Returns the milliseconds in the specified date according to universal time.                                            |
| getUTCMinutes()      | Returns the minutes in the specified date according to universal time.                                                 |
| getUTCMonth()        | Returns the month in the specified date according to universal time.                                                   |
| getUTCSeconds()      | Returns the seconds in the specified date according to universal time.                                                 |
| getYear()            | Returns the year in the specified date according to local time. Use getFullYear instead.                               |
| setDate()            | Sets the day of the month for a specified date according to local time.                                                |
| setFullYear()        | Sets the full year for a specified date according to local time.                                                       |
| setHours()           | Sets the hours for a specified date according to local time.                                                           |
| setMilliseconds()    | Sets the milliseconds for a specified date according to local time.                                                    |
| setMinutes()         | Sets the minutes for a specified date according to local time.                                                         |
| setMonth()           | Sets the month for a specified date according to local time.                                                           |
| setSeconds()         | Sets the seconds for a specified date according to local time.                                                         |
| setTime()            | Sets the Date object to the time represented by a number of milliseconds since January 1, 1970, 00:00:00 UTC.          |
| setUTCDate()         | Sets the day of the month for a specified date according to universal time.                                            |
| setUTCFullYear()     | Sets the full year for a specified date according to universal time.                                                   |
| setUTCHours()        | Sets the hour for a specified date according to universal time.                                                        |
| setUTCMilliseconds() | Sets the milliseconds for a specified date according to universal time.                                                |
| setUTCMinutes()      | Sets the minutes for a specified date according to universal time.                                                     |
| setUTCMonth()        | Sets the month for a specified date according to universal time.                                                       |
| setUTCSeconds()      | Sets the seconds for a specified date according to universal time.                                                     |
| setYear()            | Sets the year for a specified date according to local time. Use setFullYear instead.                                   |
| toDateString()       | Returns the "date" portion of the Date as a human-readable string.                                                     |
| toGMTString()        | Converts a date to a string, using the Internet GMT conventions. Use toUTCString instead.                              |
| toLocaleDateString() | Returns the "date" portion of the Date as a string, using the current locale's conventions.                            |
| toLocaleFormat()     | Converts a date to a string, using a format string.                                                                    |
| toLocaleString()     | Converts a date to a string, using the current locale's conventions.                                                   |
| toLocaleTimeString() | Returns the "time" portion of the Date as a string, using the current locale's conventions.                            |
| toSource()           | Returns a string representing the source for an equivalent Date object; you can use this value to create a new object. |
| toString()           | Returns a string representing the specified Date object.                                                               |
| toTimeString()       | Returns the "time" portion of the Date as a human-readable string.                                                     |
| toUTCString()        | Converts a date to a string, using the universal time convention.                                                      |
| valueOf()            | Returns the primitive value of a Date object.                                                                          |

## Date Static Methods

| Method       | Description                                                                                                         |
| ------------ | ------------------------------------------------------------------------------------------------------------------- |
| Date.parse() | Parses a string representation of a date and time and returns the internal millisecond representation of that date. |
| Date.UTC()   | Returns the millisecond representation of the specified UTC date and time.                                          |

## Example
```js
const date = new Date()
console.log(date)  // 
```

```js
const date = new Date("August 19, 2024 09:30:54")
console.log(date)
```

```js
let date = new Date(999999999999)
console.log(date)

date = new Date(999999999999)
console.log(date)
```

```js
const date = new Date(2001, 5, 14, 6, 43, 58, 342)
console.log(date)
```