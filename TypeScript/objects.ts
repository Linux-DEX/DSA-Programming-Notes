
const User = {
    name: 'linuxdex',
    email: 'linux@linux.com',
    isActive: true 
}

function createUser({name: string, isPaid: boolean}) {}

createUser({ name: 'linuxdex', isPaid: false })

function createCourse(): { name: string, price: number} {
    return {
        name: 'linux',
        price: 399
    }
}

type clientUser = {
    name: string,
    email: string,
    isActive: boolean
}

function createClientUser(user: clientUser): clientUser {
    return { name: '', email: '', isActive: true}
}

createClientUser({ name: '', email: '', isActive: true })


type adminUser = {
    readonly _id: string 
    name: string 
    email: string
    isActive: boolean
    credcardDetails?: number
}

let myUser: adminUser = {
    _id: '123',
    name: 'linuxdex',
    email: 'l@l.com',
    isActive: false
}

myUser.email = 'h@gmail.com'
// not allowed
// myUser._id = "2l343"

type cardNumber = {
    cardnumber: string 
}

type cardDate = {
    cardDate: string
}

type cardDetails = cardNumber & cardDate & {
    cvv: number
}

