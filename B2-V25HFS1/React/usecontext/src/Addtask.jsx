// import React, { useContext } from 'react'
// import Ct from './Ct'


// const Addtask = () => {

//   let obj=useContext(Ct)
//   return (
//     <div>
//       <input type="text" placeholder='Enter-Task' onChange={(e)=>obj.dispatch({"type":"task","payload":e.target.value})} value={obj.state.task}/>

//       <button onClick={()=> obj.dispatch({"type":"arr"})}>ADD</button>
//     </div>
//   )
// }

// export default Addtask


import React, { useContext } from 'react'
import Ct from './Ct'

const Addtask = () => {

  let obj = useContext(Ct)

  return (
    <div>

      <input
        type="text"
        placeholder="Name"
        value={obj.state.name}
        onChange={(e) => obj.dispatch({ type: "update", field: "name", value: e.target.value })}
      />

      <br />

      <input
        type="email"
        placeholder="Email"
        value={obj.state.email}
        onChange={(e) => obj.dispatch({ type: "update", field: "email", value: e.target.value })}
      />

      <br />

      <input
        type="text"
        placeholder="Address"
        value={obj.state.address}
        onChange={(e) => obj.dispatch({ type: "update", field: "address", value: e.target.value })}
      />

      <br />

      Gender:
      <input
        type="radio"
        name="g"
        value="Male"
        checked={obj.state.gender === "Male"}
        onChange={(e) => obj.dispatch({ type: "update", field: "gender", value: e.target.value })}
      /> Male

      <input
        type="radio"
        name="g"
        value="Female"
        checked={obj.state.gender === "Female"}
        onChange={(e) => obj.dispatch({ type: "update", field: "gender", value: e.target.value })}
      /> Female

      <br />

      <select
        value={obj.state.stateName}
        onChange={(e) => obj.dispatch({ type: "update", field: "stateName", value: e.target.value })}
      >
        <option value="">Select State</option>
        <option value="Andhra Pradesh">Andhra Pradesh</option>
        <option value="Telangana">Telangana</option>
        <option value="Tamil Nadu">Tamil Nadu</option>
        <option value="Karnataka">Karnataka</option>
      </select>

      <br /><br />

      <button onClick={() => obj.dispatch({ type: "add" })}>ADD</button>

    </div>
  )
}

export default Addtask
