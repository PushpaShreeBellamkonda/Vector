import {Link} from 'react-router-dom'
const Nav = () => {
  return (
    <div className="nav">
        <Link to="/">Home</Link>
        <Link to="/login">Login</Link>
        <Link to="/reg">Register</Link>
        <Link to="/about">About</Link>
    </div>
  )
}

export default Nav

