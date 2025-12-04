import { useState } from "react"

let App=()=>{
    let [c,setC]=useState(0)
    let [iid,setIId]=useState(-1)
    let inc=()=>{
        setC((prev)=>prev+1)
    }
    let start=()=>{
        if(iid==-1){
            setIId(setInterval(inc,1000))
        }
    }
    let stop=()=>{
        clearInterval(iid)
        setIId(-1)
    }
    let reset=()=>{
        stop()
        setC(0)
    }
    return(
        <div>
        <h1>{c}</h1>
        <button onClick={start}>start</button>
        <button onClick={stop}>stop</button>
        <button onClick={reset}>reset</button>
        </div>
    )
}
export default App