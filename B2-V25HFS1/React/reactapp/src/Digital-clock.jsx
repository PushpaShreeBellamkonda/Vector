import { useEffect, useState } from "react"

let App=()=>{
    let [time,setTime]=useState(new Date())
    let fun=()=>{
        setTime(new Date())
    }
    useEffect(()=>{
        setInterval(fun,1000)
    },[])
    return(
        <div>
            <h1>{time.toLocaleTimeString()}</h1>
            {/* <button onClick={fun}>get Time</button> */}
        </div>
    )
}
export default App
