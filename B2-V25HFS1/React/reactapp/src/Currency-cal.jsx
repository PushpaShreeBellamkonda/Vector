import { useState } from "react"
const App=()=>{
    let [amt,setAmt]=useState("")
    let [i,setI]=useState(0)
    let a=[1,1/86,1/103,1/11,1/45,1/2.3]
    let fun=(e)=>{
        setAmt(e.target.value)
    }
    let fun1=(e)=>{
        setI(e.target.value)
    }
    return(
        <div>
            <input type="text" placeholder="enter amount" onChange={fun} />
            <select onChange={fun1} value={i}>
                <option value="0" disabled>Rs</option>
                <option value="1">Di</option>
                <option value="2">Er</option>
                <option value="3">Vr</option>
                <option value="4">Au</option>
                <option value="5">Bh</option>
            </select>
            <div>
                {amt*a[i]}
            </div>
        </div>
    )
}
export default App
