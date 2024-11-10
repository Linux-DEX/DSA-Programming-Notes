
class User {
    email: string
    name: string 
    city: string = ''
    // this will make city readonly
    // readonly city: string = ''
    constructor(email: string, name: string) {
        this.email = email;
        this.name = name;
    }
}

const linuxdex = new User( 'l@linuxdex.com', 'linuxdex')
// not allowed because city is string
// linuxdex.city = 2 
linuxdex.city = 'bangaluru'


export {}