
interface User {
    readonly dbId: number,
    email: string, 
    userId: number,
    googleId?: string,
    // string return type of func startTrail
    // startTrail: () => string
    startTrail(): string
    getCoupon(couponname: string, value: number): number
}

interface User {
    githubToken: string
}

// Admin will inherit the User property
interface Admin extends User {
    role: 'admin' | 'ta' | 'learner'
}

const linuxdex: Admin = {
    dbId: 22, email: 'l@l.com', userId: 141,
    role: "admin",
    githubToken: "linuxdextoken",
    startTrail: () => {
        return 'trail started'
    },
    // don't need to match same as couponname
    getCoupon: (name: 'linuxdex', off: 10) => {
        return 10
    }
 }

// const linuxdex: User = {
//     dbId: 22, email: 'l@l.com', userId: 141,
//     githubToken: "linuxdextoken",
//     startTrail: () => {
//         return 'trail started'
//     },
//     // don't need to match same as couponname
//     getCoupon: (name: 'linuxdex', off: 10) => {
//         return 10
//     }
//  }

linuxdex.email = "l@linux.com"
// readonly property
// linuxdex.dbId = 33

