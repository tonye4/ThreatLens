import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import SearchParams from "./components/SearchParams";
import Consent from "./components/DataConsent";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Results from "./pages/Results";
import Navbar from "./components/Navbar";

const App = () => {
    const [openModal, setOpenModal] = useState(true); 

    return (
        <BrowserRouter>
        <div className="App">
            <Navbar />
            {/*conditionally rendering modal*/}
            {openModal && <Consent setOpenModal={setOpenModal} />}
            <Routes>
                <Route path="/" element={<SearchParams />} />
                <Route path="/consent" element={<Consent />} />
                <Route path="/Results" element={<Results />} />
            </Routes>
        </div>
        </BrowserRouter>
    );
};

const container = document.getElementById("root");
const root = createRoot(container); 
root.render(<App />);