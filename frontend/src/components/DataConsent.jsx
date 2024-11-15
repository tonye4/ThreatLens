import { useState } from "react";
import "./consentModal.css"

function Consent({setOpenModal}){
    const openInNewTab = url => {
        window.open(url, 'blank', 'noopener noreferrer')
    }
    return( 
        <div className="consentModal-bg">
            <div className="modalContainer">
                <div className="title">
                    <h1>Privacy & Data Consent</h1>
                </div>
                <div className="body">
                    <h2>Your privacy is important to us.</h2>
                    <ul>
                        <li><b>What we collect:</b> Your online username, age and information that pertains to your experience with online harrasment.</li>
                        <li><b>Why we collect it:</b> This helps us track incidents and identify harrasment patterns.</li>
                        <li><b>How we use it:</b> Your information will only be used for the purpose of tracking threats and harrasment, and will never be shared with third parties without your permission.</li>
                    </ul>
                    <p>By continuing, you agree with the information shared above. If you're unsure, feel free to read our full privacy policy for more details.</p>
                </div>
                <div className="footer">
                    <button
                        onClick={(e) => {
                            openInNewTab('https://www.youtube.com/watch?v=DKF2-zCNJ0A') // heheh :^)
                        }}
                    >Policy</button>
                    <button
                        onClick={(e) => {
                            setOpenModal(false); 
                        }}
                    >Continue</button>
                </div>
           </div> 
        </div>
    );
};

export default Consent; 