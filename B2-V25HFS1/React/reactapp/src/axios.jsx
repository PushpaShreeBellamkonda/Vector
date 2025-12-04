// 'https://fakestoreapi.com/users'

import axios from "axios"
import { useState,useEffect } from "react"

let App=()=>{
    let [data,setData]=useState([])
    useEffect(()=>{
        axios.get('https://fakestoreapi.com/users').
        then((res)=>{
            setData(res.data)
        })
    },[])
    return(
<div>
            <table border={1}>
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

        </table>
</div>
    )
}
export default App