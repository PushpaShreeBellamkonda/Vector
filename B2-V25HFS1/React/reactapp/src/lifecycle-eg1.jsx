import { useEffect, useState } from "react";
let App=()=>{
    let [c1,setC1]=useState(0)
    let [c2,setC2]=useState(0)
    let fun=()=>{
        setC1(c1+1)
    }
    let fun1=()=>{
        setC2(c2+1)
    }

    
    useEffect(()=>{
        console.log("component mounted")
        return()=>{
            console.log("component unmounted")
        }
    },[])
    useEffect(()=>{
        console.log("component updated")
    },[c1,c2])


        return(
        <div>
            <h1>{c1}</h1>
            <button onClick={fun}>inc</button>
            <h1>{c2}</h1>
            <button onClick={fun1}>inc</button>
        </div>
    )
}
export default App