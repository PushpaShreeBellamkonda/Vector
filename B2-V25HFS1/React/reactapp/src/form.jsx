// when user add details in form and click on add button , user details will appear in a table below

import { useState } from "react";
const App=()=>{
    let [data,setData]=useState({"name":" ","email":" ","dob":" ","gender":" ","state":" "})
    let fun=((e)=>{
        setData({...data,[e.target.name]:e.target.value})
    })

    let [arr,setarr]=useState([])
    let add=()=>{
        setarr([...arr,data])
        setData({'name':" ",email:" ",dob:" ",gender:" ",state:" "})
    }
        return(
            <div>
                <div className="con">
                    <input type="text" placeholder="enter name" name="name" onChange={fun} value={data.name}/>
                    <input type="email" placeholder="enter email" name="email" onChange={fun} value={data.email} />
                    <input type="date" name="dob" onChange={fun} value={data.dob} />
                    <div>
                        <input type="radio" name="gender" value="male" onChange={fun} checked={data.gender=='male'}/>Male
                        <input type="radio" name="gender" value="female" onChange={fun} checked={data.gender=='female'} />Female
                    </div>
                    <select name="state" onChange={fun} value={data.state}>
                    <option value="" selected disabled>---select---</option>
                    <option value="ap">Ap</option>
                    <option value="up">Up</option>
                    <option value="mp">Mp</option>
                    <option value="hp">Hp</option>
                    </select>
                    <button onClick={add}>Add</button>
                    {arr.length>0&&<table border={1}>
                            <tr><th>SNO</th><th>Name</th><th>Email</th><th>DOB</th><th>Gender</th><th>State</th></tr>
                            {
                                arr.map((obj,i)=>{
                                    return(
                                        <tr>
                                            <td>{i+1}</td>
                                            <td>{obj.name}</td>
                                            <td>{obj.email}</td>
                                            <td>{obj.dob}</td>
                                            <td>{obj.gender}</td>
                                            <td>{obj.state}</td>
                                        </tr>
                                    )
                                })
                            }
                        </table>}
                </div>
            </div>
        )
}
export default App

