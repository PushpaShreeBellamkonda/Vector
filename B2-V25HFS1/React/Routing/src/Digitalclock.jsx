import { useState,useEffect } from "react"
import "./App.css"
const Digitalclock = () => {
    let [time,setTime]=useState(new Date())
    let fun=()=>{
        setTime(new Date())
    }
    useEffect(()=>{
        setInterval(fun,1000)
    })
  return (
    <div className="dig">
        <p>{time.toLocaleTimeString()}</p>
    </div>
  )
}

export default Digitalclock
