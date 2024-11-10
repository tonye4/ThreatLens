import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import SearchParams from "./components/SearchParams";
import Consent from "./components/DataConsent";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Results from "./pages/Results";
import Navbar from "./components/Navbar";
import axios from "axios";
import { useEffect } from "react";

const App = () => {
    const [openModal, setOpenModal] = useState(true);

        useEffect(() => {
        axios.post("http://127.0.0.1:8000/api/comments")
            .then((response) => {
                console.log("Ping successful:", response);
            })
            .catch((error) => {
                console.error("There was an error reaching the server", error);
            });
    }, []);

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