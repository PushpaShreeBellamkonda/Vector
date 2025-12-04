let d=new Date()
console.log(d)
console.log(d.toLocaleDateString())
console.log(d.toLocaleTimeString())
let fun=()=>{
    console.log("hello")
}
let iid=setInterval(fun,1000)

let stop=()=>{
    clearInterval(iid)
}
setTimeout(stop,10000)