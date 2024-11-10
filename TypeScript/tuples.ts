
// const user: ( string | number )[] = [ 1, "hc" ]

let user: [string, number, boolean] 

user = [ "hc", 123, false ]
// it should be in order
// user = [ 123, false, "hc" ]

let rgb: [ number, number, number ] = [ 255, 123, 233 ]
// this is not allowed it should be only 3 number
// let rgb: [ number, number, number ] = [ 255, 123, 233, 0.5 ]

type User = [ number, string ]

const newUser: User = [ 112, "example@gmail.com" ]
newUser[1] = "hc.com"
// with this we can add new value so be carefull while using tuples
// newUser.push(true)

export {}