import './App.css'
function App(){
  let name='pushpa'
  let place='hyderabad'
  let a=3,b=9;
    return(
      <div>
        <p>{name} is from {place}</p>
        <p> sum of {a} and {b} is {a+b} </p>
      </div>
    )
}
// export default App

function App1(){
  let obj={"name":"pushpa","age":21,"dept":"cse","gpa":8.9}
  return (<table border={1}>
        <tr><th>Name:</th><td>{obj.name}</td></tr>
        <tr><th>Age:</th><td>{obj.age}</td></tr>
        <tr><th>Department:</th><td>{obj.dept}</td></tr>
        <tr><th>GPA:</th><td>{obj.gpa}</td></tr>
  </table>)
}

// export default App1
import './App.css'
function App2(){
  let prod={"title":"Doraemon","price":"30$","desc":"Most lovable cat in the world","img":"https://cdn.pixabay.com/photo/2013/01/09/17/56/doraemon-74473_640.jpg"}
  return(
    <div className="dora">
      <img src={prod.img}/>
      <p>Price:{prod.price}</p>
      <p>Description:{prod.desc}</p>
    </div>
  )
}
export default App2