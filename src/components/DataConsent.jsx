import { useState } from "react";
//import "./consentModal.css"

function Consent(){
    const[openModal, setOpenModal] = useState(true); // want it to be open on first page load, so set state to true.
    if(openModal != true)
        return null;

    return( 
        <div className="consentModal-bg">
            <div className="ModalContainer">
                <div className="Title">
                    <h1>Privacy & Data Consent</h1>
                </div>
                <div className="body">
                    <h2>Your privacy is important to us.</h2>
                    <ul>
                        <li>What we collect: Your online username, age and information that pertains to your experience with online harrasment.</li>
                        <li>Why we collect it: This helps us track incidents and identify harrasment patterns.</li>
                        <li>How we use it: Your information will only be used for the purpose of tracking threats and harrasment, and will never be shared with third parties without your permission.</li>
                    </ul>
                    <h2>By continuing, you agree with the information shared above. If you're unsure, feel free to read our full privacy policy for more details.</h2>
                </div>
                <div className="footer">
                    <button>Learn More</button>
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