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

  const [backendMessage, setBackendMessage] = useState('');

  useEffect(() => {
    // Function to fetch data from the Django backend
    const checkConnection = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/test/');
        console.log(response);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setBackendMessage(data.message); // Set the message from backend
      } catch (error) {
        console.error('Error fetching data:', error);
        setBackendMessage('Error communicating with backend');
      }
    };

    checkConnection();
  }, []);

    return (
        <BrowserRouter>
        <div className="App">
    <div className="App">
      <h1>React-Django Communication Test</h1>
      <p>{backendMessage ? backendMessage : 'Loading...'}</p>
    </div>
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