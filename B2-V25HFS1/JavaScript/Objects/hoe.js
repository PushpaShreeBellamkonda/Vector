
// 1. Filter out people who are under 18.
const people = [
  { name: "John", age: 17 },
  { name: "Jane", age: 22 },
  { name: "Jim", age: 15 },
  { name: "Jack", age: 19 }
];

let filarr=people.filter((val,ind,arr)=>{
            return val.age<18
})

console.log(filarr)

/* 2.
add gst
filter based on rating
total inventory cost
sort by price and rating
check stock
verify ratings
*/

const products = [
  { name: "Laptop", price: 70000, rating: 4.5, inStock: true },
  { name: "Phone", price: 35000, rating: 4.2, inStock: true },
  { name: "Tablet", price: 25000, rating: 3.8, inStock: true },
  { name: "Headphones", price: 4000, rating: 4.8, inStock: true },
  { name: "Smartwatch", price: 15000, rating: 4.0, inStock: false },
];
// 1
let gst=products.map((val,ind,arr)=>{
    return{
        ...val,
        gst:val.price*0.2
    }
})
console.log(gst)
// 2
let hightrat=products.filter((val)=>{
    return val.rating>4.4
})
console.log(hightrat)
// 3
let tot=products.reduce((acc,v)=>{
        return acc+v.rating
},0)
console.log(tot)
// 4
let srt=[...products].sort((a,b)=>{
    if (a.price!=b.price){
        return a.price-b.price
    }
    return a.rating-b.rating
})
console.log(products)
console.log(srt)
// 5
stk=products.filter((val,ind,arr)=>{
        return val.inStock
})
console.log(stk)

/* 
3.Tasks:
map: Add a new key total = price * quantity.
filter: Show items where price > 1000.
reduce: Find total bill amount.
some: Check if any item costs more than ₹2000.
every: Check if all quantities > 0.
sort: Sort items by price (low → high).
*/

const cart = [
  { item: "Shoes", price: 1500, quantity: 2 },
  { item: "Bag", price: 800, quantity: 1 },
  { item: "Watch", price: 3000, quantity: 1 }
];

// 1
tot=cart.map((val,ind)=>{
    return{
        ...val,
        total:val.price*val.quantity
    }
})
console.log(tot)
// 2
maxprice=cart.filter((val,ind)=>{
    return val.price>1000
})
console.log(maxprice)

// 3
bill=cart.reduce((acc,val)=>{
    return acc+val.price
},0)
console.log(bill)

// 4
x=cart.some((val)=>{
    return val.price>2000
})
console.log(x)

y=cart.every((val)=>{
    return val.quantity>1
})
console.log(y)

s=cart.sort((a,b)=>{
    return a.price-b.price
})
console.log(s)