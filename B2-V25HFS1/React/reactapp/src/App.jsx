import { useState } from "react";
let App=()=>{
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
export default App