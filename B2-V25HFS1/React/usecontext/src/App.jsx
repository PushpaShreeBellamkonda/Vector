// import React, { useReducer } from 'react'
// import Ct from './Ct'
// import Addtask from './Addtask'
// import Disp from './Disp'



// const App = () => {
//   let[state,dispatch]=useReducer((state,action)=>{
//     if(action.type=="task"){
//       return{...state,"task":action.payload}
//     }

//     else{
//       return{"arr":[...state.arr,state.task],"task":""}

//     }

//   },{"task":"","arr":[]})
//   let obj={"state":state,"dispatch":dispatch}
  
//   return (
//     <div>
//       <Ct.Provider value={obj}>
//         <Addtask/>
//         <Disp/>


//       </Ct.Provider>

//     </div>
//   )
// }

// export default App


import React, { useReducer } from 'react'
import Ct from './Ct'

import Addtask from './Addtask'
import Disp from './Disp'

const App = () => {

  let [state, dispatch] = useReducer((state, action) => {

    if (action.type == "update") {
      return { ...state, [action.field]: action.value }
    }

    if (action.type == "add") {
      let newObj = {
        name: state.name,
        email: state.email,
        address: state.address,
        gender: state.gender,
        stateName: state.stateName
      }
      return {
        ...state,
        arr: [...state.arr, newObj],
        name: "",
        email: "",
        address: "",
        gender: "",
        stateName: ""
      }
    }

    return state
  },
    {
      name: "",
      email: "",
      address: "",
      gender: "",
      stateName: "",
      arr: []
    })

  let obj = { state, dispatch }

  return (
    <div>
      <Ct.Provider value={obj}>
        <Addtask />
        <Disp />
      </Ct.Provider>
    </div>
  )
}

export default App
