
// import React, { useContext } from 'react'
// import Ct from './Ct'


// const Disp = () => {
//   let obj=useContext(Ct)
//   return (
//     <div>
//       {obj.state.arr.length == 0 && <h1>No Tasks to Display</h1>}

//       <ul>{obj.state.arr.map((task,i)=><li key={i}>{task}</li>)}</ul>
//     </div>
//   )
// }

// export default Disp


import React, { useContext } from 'react'
import Ct from './Ct'

const Disp = () => {

  let obj = useContext(Ct)
      
  return (
    <div>

      {obj.state.arr.length === 0 && <h1>No Data to Display</h1>}

      {obj.state.arr.length > 0 &&
        <table border={1}>
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Address</th>
              <th>Gender</th>
              <th>State</th>
            </tr>
          </thead>

          <tbody>
            {obj.state.arr.map((item, i) =>
              <tr key={i}>
                <td>{item.name}</td>
                <td>{item.email}</td>
                <td>{item.address}</td>
                <td>{item.gender}</td>
                <td>{item.stateName}</td>
              </tr>
            )}
          </tbody>
        </table>
      }

    </div>
  )
}

export default Disp
