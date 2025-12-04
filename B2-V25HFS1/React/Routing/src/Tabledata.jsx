import axios from "axios"
import {useState,useEffect} from "react"
import "./App.css"
const Tabledata = () => {
    let [data,setData]=useState([])
    useEffect(()=>{
        axios.get('https://fakestoreapi.com/users').
        then((res)=>{
            setData(res.data)
    })
    },[])
  return (
    <div>
        {data.length>0 && <table border={1} className="tbl">
            <tr><th>id</th><th>email</th><th>username</th><th>password</th></tr>
            {
                data.map((obj)=>{
                    return(
                        <tr>
                            <td>{obj.id}</td>
                            <td>{obj.email}</td>
                            <td>{obj.username}</td>
                            <td>{obj.password}</td>
                        </tr>
                    )
                })
            }

        </table>}
      
    </div>
  )
}

export default Tabledata
