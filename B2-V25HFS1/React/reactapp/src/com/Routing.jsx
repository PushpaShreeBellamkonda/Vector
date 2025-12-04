import { BrowserRouter, Route, Routes } from "react-router-dom"
import Nav from "./com/Nav.jsx"
import Home from "./com/Home"
import Login from "./com/Login"
import Register from "./com/Register"
import About from "./com/About"
import Footer from "./com/Footer"
let App=()=>{
    return(
        <BrowserRouter>
        <Nav/>
        <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/login" element={<Login/>}/>
            <Route path="/reg" element={<Register/>}/>
            <Route path="/about" element={<About/>}/>
        </Routes>
        <Footer/>
        </BrowserRouter>
    )
}
export default App

// to run this add the above code in App.jsx

