import React, { useState } from "react";

const Register = () => {
  let [data, setData] = useState({name: "", dob: "", place: "", email: "", state: "", addr: "", rt: "8", gen: "", lang: [],});
  let fun1 = (e) => {
    setData({ ...data, [e.target.name]: e.target.value });
  };
  let fun2 = (e) => {
    if (e.target.checked) {
      data.lang.push(e.target.value);
    } else {
      data.lang.splice(data.lang.indexOf(e.target.value), 1);
    }
    setData({ ...data });
  };
  return (
    <div>
      <div className="form">
        <input
          type="text"
          placeholder="Enter Name"
          name="name"
          onChange={fun1}
          value={data.name}
        />
        <input
          type="text"
          placeholder="Enter Place"
          name="place"
          onChange={fun1}
          value={data.place}
        />
        <input
          type="email"
          placeholder="Enter email"
          onChange={fun1}
          name="email"
          value={data.email}
        />
        <input type="date" value={data.dob} name="dob" onChange={fun1} />
        <select value={data.state} name="state" onChange={fun1}>
          <option value="" disabled>
            ---select---
          </option>
          <option value="AP">Andhra</option>
          <option value="AR">Arunchal</option>
          <option value="AD">Adaman</option>
          <option value="TG">Telangana</option>
        </select>
        <label>Address:</label>
        <textarea
          rows={5}
          cols={10}
          value={data.addr}
          onChange={fun1}
          name="addr"
        ></textarea>
        <div>
          <input
            type="range"
            min={1}
            max={10}
            value={data.rt}
            name="rt"
            onChange={fun1}
          />
          <span>{data.rt}</span>
        </div>
        <div>
          <input
            type="radio"
            value="male"
            name="gen"
            onChange={fun1}
            checked={data.gen == "male"}
          />
          Male
          <input
            type="radio"
            value="female"
            name="gen"
            onChange={fun1}
            checked={data.gen == "female"}
          />
          FeMale
        </div>
        <div>
          <input
            type="checkbox"
            value="python"
            onChange={fun2}
            checked={data.lang.includes("python")}
          />
          Python
          <input
            type="checkbox"
            value="java"
            onChange={fun2}
            checked={data.lang.includes("java")}
          />
          Java
          <input
            type="checkbox"
            value="js"
            onChange={fun2}
            checked={data.lang.includes("js")}
          />
          js
          <input
            type="checkbox"
            value="react"
            onChange={fun2}
            checked={data.lang.includes("react")}
          />
          React
        </div>
        <p>{data.lang.toString()}</p>
      </div>
    </div>
  );
};

export default Register;