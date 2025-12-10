import { FormProvider } from "./context/FormContext";
import UserForm from "./components/UserForm";
import DataTable from "./components/DataTable";

export default function App() {
  return (
    <FormProvider>
      <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">
        <UserForm />
        <DataTable />
      </div>
    </FormProvider>
  );
}
