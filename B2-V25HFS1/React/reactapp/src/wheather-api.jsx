import { useState } from "react"
import axios from "axios"

let App=()=>{
    let [place,setPlace]=useState("")
    let [data,setData]=useState("")
    let [err,setErr]=useState("")
        let fun=(e)=>{
                setPlace(e.target.value)
        }
        let getdata=()=>{
            axios.get(`http://api.weatherapi.com/v1/current.json?key=73bf391368364da09ed50810252711&q=${place}&aqi=no`).
            then((res)=>{
                        setData(res.data)
                        setErr("")
                        setPlace("")
            }).catch(()=>{
                    setErr("check place name")
                    setData("")
            })
        }
    return(
            <div>

                <input type="text" placeholder="enter place" onChange={fun} value={place} />
                <button onClick={getdata}>Get dtailes</button>
                    {
                    data!=""&&<div className="tempcard">
                    <p>Name:{data.location.name}</p>
                    <p>Region:{data.location.region}</p>
                    <p>Condition:{data.current.condition.text}</p>
                    <p>Temp:{data.current.temp_c}</p>
                    <p>Feelslike:{data.current.feelslike_c}</p>
                    </div>
                    }

                    {
                    err!=""&& <div>{err}</div>
                    }
            </div>
    )
}
export default App