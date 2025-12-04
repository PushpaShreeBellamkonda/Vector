// Higher order functions
// 1.forEach
let arr=['html','css','js']
arr.forEach((val,ind,arr)=>{
    console.log(val)
    // console.log(ind)
    // console.log(arr)
})

// 2.map
let arr1=['html','css','js']
let newarr=arr.map((val,ind,arr)=>{
    return 'FET-'+val
})
console.log(newarr)

// 
let a=[1,2,3,44,]
let d=a.map((v)=>v+v)
console.log(d)

// 3.filter
let b=[1,2,3,4,7,9]
let f=b.filter((v)=>{
    return v%2==1
})
console.log(f)
// 
let data=[
    {name:'john',age:20,branch:"cse"},{name:'rose',age:21,branch:"eee"},{name:'jack',age:22,branch:"cse"}
]
let fdata=data.filter((v)=>{
    return v.age>20
})
console.log(fdata)

// 4.reduce
let arr2=[8,7,5,9,8,3]
let tot=arr2.reduce((acc,v)=>{
        return acc+v
})
console.log(tot)

//  to create a new array that contains only words with 5 or fewer characters.
let words=['hello','javascript','pushpa','five','characters']
let farr=[]
    words.filter((val,ind,arr)=>{
        return farr.push(val.length<=5)
})
console.log(farr)

// Calculate the average of an array of numbers.
let array=[8,7,5,9,8,3]
let red=array.reduce((acc,v)=>{
        return (acc+v)
},0)
console.log(red/array.length)

// First double the numbers using map,
// Then filter only those above 60.
l=[10, 25, 30, 45, 50]
ll=l.map((v)=>v+v)
console.log(ll.filter((val,ind)=>{
    return val>60
}))

// filter only even numbers and find their sum.
l=[10, 25, 30, 45, 50]
l1=l.filter((val,ind)=>{
    return val%2==0
})
console.log(l1)
l2=l1.reduce((acu,val)=>{
        return acu+val
},0)
console.log(l2)
