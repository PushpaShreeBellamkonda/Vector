import { createContext, useContext, useReducer } from "react";


const FormContext = createContext();


const initialState = {
    records: [],
};


function formReducer(state, action) {
    switch (action.type) {
        case "ADD_RECORD":
            return {
                ...state,
                records: [...state.records, action.payload],
            };


        default:
            return state;
    }
}


export function FormProvider({ children }) {
    const [state, dispatch] = useReducer(formReducer, initialState);


    return (
        <FormContext.Provider value={{ state, dispatch }}>
            {children}
        </FormContext.Provider>
    );
}


export function useFormContext() {
    return useContext(FormContext);
}