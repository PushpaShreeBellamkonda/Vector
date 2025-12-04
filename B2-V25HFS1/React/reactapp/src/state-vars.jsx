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

// state variables : when we type smtg on input field it should reflect below in h3 tag

import { useState } from "react"
let App1=()=>{
    let [data,setData]=useState("")
    let fun=(event)=>{
        setData(event.target.value)
    }
    return(
        <div>
            <input type="text" onChange={fun} />
            <h3>{data}</h3>
        </div>
    )
}
// export default App

// state variable : factorial of a number

import { useState } from "react";
let App2=()=>{
    let [n,setN]=useState(" ")
    let [f,setF]=useState(" ")
    let fun=(event)=>{
        setN(event.target.value)
    }
    let fac=()=>{
        f=1
        for (let i=1;i<=parseInt(n);i++){
            f=f*i
        }
        setF(f)
        setN(" ")
    }
    return(
        <div>
            <input type="text" onChange={fun} value={n} />
            <button onClick={fac}>Get Factorial</button>
            <h1>{f}</h1>
        </div>
    )
}
// export default App

// state variable: when user enter smtg on input they should be reflecte as list elements

import { useState } from "react";
let App3=()=>{
    let [data,setData]=useState(" ")
    let [a,setA]=useState([])
    let fun=(event)=>{
        setData(event.target.value)
    }
    let add=()=>{
        setA([...a,data])
        setData(" ")
    }
    return(
        <div>
            <input type="text" onChange={fun} value={data} />
            <button onClick={add}>Add</button>
            <ul>
                {
                    a.map((str)=><li>{str}</li>)
                }
            </ul>
        </div>
    )
}
// export default App

// next one is form.jsx

