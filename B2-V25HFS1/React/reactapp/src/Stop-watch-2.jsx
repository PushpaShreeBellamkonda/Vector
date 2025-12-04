import { useEffect, useState } from "react"

let App = () => {
    let [c, setC] = useState(0)
    let [m, setM] = useState(0)
    let [h, setH] = useState(0)
    let [iid, setIId] = useState(-1)
    let inc = () => {
        setC((prev) => prev + 1)
    }
    let start = () => {
        if (iid == -1) {
            setIId(setInterval(inc, 1000))
        }
    }
    let stop = () => {
        clearInterval(iid)
        setIId(-1)
    }
    let reset = () => {
        stop()
        setC(0)
        setM(0)
        setH(0)
    }
    useEffect(() => {
        if (c == 60) {
            setC(0)
            setM(m + 1)
        }
    }, [c])
    useEffect(() => {
        if (m == 60) {
            setM(0)
            setH(h + 1)
        }
    }, [m])
    return (
        <div>
            <h1>{h < 10 ? "0" + h : h}:{m < 10 ? "0" + m : m}:{c < 10 ? "0" + c : c}</h1>
            <button onClick={start}>start</button>
            <button onClick={stop}>stop</button>
            <button onClick={reset}>reset</button>
        </div>
    )
}
export default App