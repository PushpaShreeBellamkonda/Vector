import { useState ,useEffect} from "react"
import "./App.css"
const Stopwatch = () => {
    let [c,setC]=useState(0)
    let [m,setM]=useState(0)
    let [h,setH]=useState(0)
    let [iid,setIid]=useState(-1)

    let inc=()=>{
        setC((prev)=>prev+1)
    }
    let start=()=>{
        if(iid==-1){
            setIid(setInterval(inc,1000))
        }
    }
    let stop=()=>{
        clearInterval(iid)
        setIid(-1)
    }
    let reset=()=>{
        stop()
        setC(0)
        setM(0)
        setH(0)
    }
    useEffect(()=>{
            if(c==60){
                setC(0)
                setM(m+1)
            }
    },[c])
    useEffect(()=>{
        if(m==60){
            setM(0)
            setH(h+1)
        }
    },[m])
  return (
    <div className="stp">
        <h1>{h}:{m}:{c}</h1>
        <button onClick={start}>start</button>
        <button onClick={stop}>stop</button>
        <button onClick={reset}>reset</button>

    </div>
  )
}

export default Stopwatch
