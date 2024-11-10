/*

syntax:

let variableName: type = value

*/

let greetings: string = 'hello linuxdex';

// This will not allowed in typescript
// greetings = true; 

console.log(greetings);

let mynum = 6 

// it will not all string method on number 
// mynum.toUpperCase()

// number 

let userId: number = 334455 


// boolean 

let isLoggedIn: boolean = false 

// any

let hero;

function getHero() {
    return 'thor'
}

hero = getHero();