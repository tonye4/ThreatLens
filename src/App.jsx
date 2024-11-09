import React from "react";
import { createRoot } from "react-dom/client";
import SearchParams from "./components/SearchParams";
import Consent from "./components/DataConsent";

// TODO: Create forum search params 
// TODO: Make do you consent form that pops up before forum

const App = () => {
    return (
        <div className="App">
            <SearchParams />
            <Consent />
        </div>
    );
};

const container = document.getElementById("root");
const root = createRoot(container); 
root.render(<App />);