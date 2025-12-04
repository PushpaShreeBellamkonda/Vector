import {Link} from 'react-router-dom'
import "./App.css"
const Nav = () => {
  return (
    <div className='navbar'>
      <Link to="/stpw">StopWatch</Link>
      <Link to="/tbl">TableData</Link>
      <Link to="/Digclk">DigitalClock</Link>
    </div>
  )
}
export default Nav
