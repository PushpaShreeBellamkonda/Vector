import { useFormContext } from "../context/FormContext";


export default function DataTable() {
const { state } = useFormContext();


if (state.records.length === 0) {
return <p className="mt-6 text-gray-500">No records added yet.</p>;
}


return (
<div className="mt-8 w-full max-w-4xl overflow-x-auto">
<table className="w-full border border-collapse" border={1}>
<thead>
<tr className="bg-gray-200">
<th className="border p-2">Name</th>
<th className="border p-2">Email</th>
<th className="border p-2">Age</th>
<th className="border p-2">Course</th>
</tr>
</thead>
<tbody>
{state.records.map((item, index) => (
<tr key={index} className="text-center">
<td className="border p-2">{item.name}</td>
<td className="border p-2">{item.email}</td>
<td className="border p-2">{item.age}</td>
<td className="border p-2">{item.course}</td>
</tr>
))}
</tbody>
</table>
</div>
);
}