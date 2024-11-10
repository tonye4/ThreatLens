import { useState } from 'react'; 
import { Link } from 'react-router-dom';
import './Navbar.css'

export default function Navbar() {
    const [fix, setFix] = useState(false)

    // when we scroll to a certain height on the Y-axi
    function setFixed(){
        if(window.scrollY >= 200) {
            setFix(true);
        } else {
            setFix(false);
        }
    }

    window.addEventListener("scroll", setFixed)
    return (
        <header>
            <nav className="navbar">
                <ul>
                    <li>
                        <a href="/"><img src="./../img/Threat_Lens_thin.png" alt="Threat Lens logo"/></a>
                    </li>
                    <li><a href="/">Home</a></li> {/*using routing in our navbar.*/}
                    <li><a href="#hero">About</a></li>
                    <li><a href="#getting-started">Getting Started</a></li>
                </ul>
            </nav>
        </header>
    )
}