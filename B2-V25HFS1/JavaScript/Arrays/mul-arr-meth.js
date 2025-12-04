/* 
Combine multiple array methods.

1.Map + Filter:
From [10, 25, 30, 45, 50],
First double the numbers using map,
Then filter only those above 60.

2.Filter + Reduce:
From an array of numbers,
filter only even numbers and find their sum.
*/

// 1
let arr=[10, 25, 30, 45, 50]
let d=arr.map((v)=>v+v)
let a=d.filter((v)=>v>60)
console.log(a)

// 2
let arr1=[10, 25, 30, 45, 50]
let s=arr1.filter((v)=>
    {
        return v%2==0
    }
)
console.log(s)
let e=s.reduce((acc,v)=>{
        return acc+v
})
console.log(e)