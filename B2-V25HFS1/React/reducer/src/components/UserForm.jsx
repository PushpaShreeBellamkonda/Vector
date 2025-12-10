// src/components/UserForm.jsx
import { useState } from "react";
import { useFormContext } from "../context/FormContext";

export default function UserForm() {
  const { dispatch } = useFormContext();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    age: "",
    course: "",
  });

  function handleChange(e) {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  }

  function handleSubmit(e) {
    e.preventDefault();

    // basic validation
    if (!formData.name || !formData.email || !formData.age || !formData.course) {
      alert("Please fill all fields");
      return;
    }

    // dispatch an action to add the record
    dispatch({ type: "ADD_RECORD", payload: formData });

    // reset form
    setFormData({ name: "", email: "", age: "", course: "" });
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white rounded-2xl shadow-md p-6 w-full max-w-xl"
    >
      <h2 className="text-2xl font-semibold mb-4">Student Form</h2>

      <div className="grid grid-cols-1 gap-4">
        <input
          type="text"
          name="name"
          placeholder="Enter Name"
          value={formData.name}
          onChange={handleChange}
          className="border p-2 rounded"
        />

        <input
          type="email"
          name="email"
          placeholder="Enter Email"
          value={formData.email}
          onChange={handleChange}
          className="border p-2 rounded"
        />

        <input
          type="number"
          name="age"
          placeholder="Enter Age"
          value={formData.age}
          onChange={handleChange}
          className="border p-2 rounded"
        />

        <input
          type="text"
          name="course"
          placeholder="Enter Course"
          value={formData.course}
          onChange={handleChange}
          className="border p-2 rounded"
        />

        <button
          type="submit"
          className="bg-black text-white py-2 rounded hover:opacity-80"
        >
          Add
        </button>
      </div>
    </form>
  );
}
