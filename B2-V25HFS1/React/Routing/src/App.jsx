import { BrowserRouter, Route , Routes } from "react-router-dom"
import Stopwatch from "./Stopwatch"
import Tabledata from "./Tabledata"
import Digitalclock from "./Digitalclock"
import Nav from "./Nav"

let App=()=>{
    return(
      <BrowserRouter>
      <Nav/>
      <Routes>
        <Route path="/stpw" element={<Stopwatch/>}></Route>
        <Route path="/tbl" element={<Tabledata/>}></Route>
        <Route path="/Digclk" element={<Digitalclock/>}></Route>
      </Routes>
      </BrowserRouter>
    )
}
export default App