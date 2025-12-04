import { BrowserRouter, Route, Routes } from "react-router-dom"
import Nav from "./comp/Nav.Jsx"
import Home from "./comp/Home"
import Login from "./comp/Login"
import Register from "./comp/Register"
import About from "./comp/About"
import Footer from "./comp/Footer"
import './App.css'

let App=()=>{
  return(<BrowserRouter>
  <Nav/>
  <Routes>
    <Route path="/" element={<Home/>}/>
     <Route path="/login" element={<Login/>}/>
      <Route path="/reg" element={<Register/>}/>
       <Route path="/about" element={<About/>}/>

  </Routes>
  <Footer/>
  </BrowserRouter>)
}
export default App