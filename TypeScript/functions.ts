
function addTwo(num: number): number {
    return num + 2 
    // return 'hello'
}

addTwo(5)

function signUpUser(name: string, email: string, isPaid: boolean) { }

let loginUser = (username: string, password: string = 'not_needed') => {}

signUpUser('linuxdex', 'linuxdex@linux.com', false)
loginUser('linuxdex')

function getValue(myVal: number): boolean | string {
    if (myVal > 5) {
        return true
    }
    return "200 OK"
}

const getHello = (s: string): string => {
    return ''
}

// const heros = [ 'thor', 'spiderman', 'ironman' ]
const heros = [ 1, 2, 3 ]

heros.map(( hero ): string => {
    return `hero is ${hero}`
})

function consoleError(errmsg: string): void {
    console.log(errmsg);
}

function handleError(errmsg: string): never {
    throw new Error(errmsg);
}
