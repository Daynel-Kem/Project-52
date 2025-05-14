const os = require("os")
const path = require("path")

path.sep = '.'

const user = os.userInfo()
console.log(user)

console.log(`System uptime is ${os.uptime()} seconds`)

const currentOS = {
    name:os.type(),
    release:os.release(),
    totalmem:os.totalmem(),
    freemem:os.freemem()
}

console.log(currentOS)
// const names = require("./names.js")
// console.log(names)

// const foo = require("./utils.js")

// console.log(foo.foo(names.name1))

const filePath = path.join('/content', 'subfolder', 'test.txt')
console.log(filePath)


const base = path.basename(filePath)
console.log(base)

