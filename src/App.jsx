import React from "react";
import { createRoot } from "react-dom/client";

// TODO: Create a dashboard

const App = () => {
    return (
        <h1>Threat lens</h1>
    )
}

const container = document.getElementById("root");
const root = createRoot(container); 
root.render(<App />);