import './App.css'
// rendering variable data
function App() 
{
  let name = 'pushpa'
  let place = 'hyderabad'
  let a = 3, b = 9;
  return (
    <div>
      <p>{name} is from {place}</p>
      <p> sum of {a} and {b} is {a + b} </p>
    </div>
  )
}
// export default App

// rendering object data
function App1() {
  let obj = { "name": "pushpa", "age": 21, "dept": "cse", "gpa": 8.9 }
  return (<table border={1}>
    <tr><th>Name:</th><td>{obj.name}</td></tr>
    <tr><th>Age:</th><td>{obj.age}</td></tr>
    <tr><th>Department:</th><td>{obj.dept}</td></tr>
    <tr><th>GPA:</th><td>{obj.gpa}</td></tr>
  </table>)
}
// export default App1

// rendering product data
import './App.css'
function App2() {
  let prod = { "title": "Doraemon", "price": "30$", "desc": "Most lovable cat in the world", "img": "https://cdn.pixabay.com/photo/2013/01/09/17/56/doraemon-74473_640.jpg" }
  return (
    <div className="dora">
      <img src={prod.img} />
      <p>Price:{prod.price}</p>
      <p>Description:{prod.desc}</p>
    </div>
  )
}
// export default App2

// rendering array of strings
let App3 = () => {
  let arr = ["html", "css", "js", "react"]
  return (
    <div>~
      <ol>
        {
          arr.map((str) => <li>{str}</li>)
        }
      </ol>
    </div>
  )
}
// export default App3

// rendering array of objects as cards

let Arr = [
  {
    "id": 1,
    "name": "Laptop Bag",
    "price": 899,
    "brand": "Skyline",
    "rating": 4.1,
    "image": "https://picsum.photos/200?random=1"
  },
  {
    "id": 2,
    "name": "Smart Watch",
    "price": 2199,
    "brand": "FireTech",
    "rating": 4.5,
    "image": "https://picsum.photos/200?random=2"
  },
  {
    "id": 3,
    "name": "Bluetooth Speaker",
    "price": 1599,
    "brand": "BoomBox",
    "rating": 4.0,
    "image": "https://picsum.photos/200?random=3"
  },
  {
    "id": 4,
    "name": "Gaming Headphones",
    "price": 1899,
    "brand": "SoundCore",
    "rating": 4.6,
    "image": "https://picsum.photos/200?random=4"
  },
  {
    "id": 5,
    "name": "Wireless Mouse",
    "price": 499,
    "brand": "TechBee",
    "rating": 4.2,
    "image": "https://picsum.photos/200?random=5"
  },
  {
    "id": 6,
    "name": "Power Bank",
    "price": 1299,
    "brand": "ChargeMate",
    "rating": 4.4,
    "image": "https://picsum.photos/200?random=6"
  },
  {
    "id": 7,
    "name": "USB-C Charger 25W",
    "price": 799,
    "brand": "VoltPro",
    "rating": 4.3,
    "image": "https://picsum.photos/200?random=7"
  }
]


let App4 = () => {
  return (<div className='con'>
    {
      Arr.map((card) => {
        return (
          <div className='card'>
            <img src={card.image} />
            <p>ID:{card.id}</p>
            <p>NAME:{card.name}</p>
            <p>PRICE:{card.price}</p>
            <p>BRAND{card.brand}</p>
            <p>RATING:{card.rating}</p>
            <button>ADD TO CART</button>
          </div>
        )
      }
      )
    }
  </div>)
}
// export default App4

// rendering array of objects as table
let App5=()=>{
  return(<table border={1}>
      <tr><th>IMAGE</th><th>ID</th><th>NAME</th><th>PRICE</th><th>BRAND</th><th>RATING</th></tr>
      {
              Arr.map((obj)=>{
                  return(
                    <tr><td>{obj.image}</td><td>{obj.id}</td><td>{obj.name}</td><td>{obj.price}</td><td>{obj.brand}</td><td>{obj.rating}</td></tr>
                  )
      })
      }
  </table>)
}
// export default App5

// multiple components
let App=()=>{
  return(
    <div>
      <Cmp1/>

    </div>
  )
}
// export default 

// multiple components
import Cmp1 from "./Cmp1"
import Cmp2 from "./Cmp2"
import Cmp3 from "./Cmp3"

let App=()=>{
  return(
    <div>
      <Cmp1/>
      <Cmp2/>
      <Cmp3/>

    </div>
  )
}
// export default App

// Props
import Disp from './Disp'
import Disp1 from './Disp1'
let App=()=>{
  let name="pushpa"
  let age=21
  let gpa=8.5
  return (
    <div>
      <Disp name={name} age={age} id="867" gpa={gpa}/>
      <Disp1 name={name} age={age} id="866" gpa={gpa}/>
    </div>
  )
}
// export default App

// customizing button component
import Btn from './Btn'
let App=()=>{
  let style1={"color":"orange","border":"2px solid yellow","padding":"5px 20px"}
  let style2={"color":"yellow","border":"2px solid orange","padding":"5px 20px"}
  return(
    <div>
    <Btn label="Click" sty={style1}/>
    <Btn label="Login" sty={style2}/>
    <Btn label="Register" sty={style1}/>
    <Btn label="Submit" sty={style2}/>
    </div>
  )
}
// export default App

// state variables increment,decrement , reset

import { useState } from "react"
let App=()=>{
    let [c,setC]=useState(0)
    let inc=()=>{
        setC(c+1)
        console.log(c)
    }
    let dec=()=>{
        if(c>0){
        setC(c-1)
        }
    }
    let res=()=>{
        setC(c=0)
    }
    return(
        <div>
            <h1>{c}</h1>
            <button onClick={inc}>Increse</button>
            <button onClick={dec}>Decrease</button>
            <button onClick={res}>Reset</button>
        </div>
    )
}
// export default App

