import { useState } from "react"; 
import "./searchParams.css"; 
import { useNavigate } from "react-router-dom";

const SearchParams = () => {
    /* make hero section last!!
    onst [inputs, setInputs] = useState({
        username: '',
        age: '',
        profession: ''
    });*/



    const navigate = useNavigate(); 

    const ETHNICITIES = ["Black", "White", "Asian", "Middle Eastern", "Indigenous"];
    const GENDER = ["Male", "Female", "Non-binary", "Other"];
    const [age, setAge] = useState(''); 
    const [username, setUsername] = useState("");  
    const [ethnicities, setEthnicities] = useState("");  
    const [gender, setGender] = useState("");
    const [occupation, setOccupation] = useState(); 

    const handleSubmit = (event) => {
        event.preventDefault(); // default action is a page reload via submit, don't want that. 
        navigate('./Results') 
    }

    return (
        <div className = "GrandpapContainer">
            <div className="heroSect" id="hero">
                <h1>Hero</h1>
            </div>
            <div className="searchParamsBg">
                <div className="searchParams" id="getting-started">
                    <form onSubmit={handleSubmit}>
                        <label htmlFor="userName">
                            Username: 
                            <input
                            type="text" 
                            name="userName" 
                            value={username} 
                            onChange={(e) => setUsername(e.target.value)} 
                            />
                        </label>
                        <label htmlFor="age">
                            Age: 
                            <input
                            type="number"
                            name="age"
                            value={age}
                            onChange={(e) => setAge(e.target.value)}
                            />
                        </label>
                        <label htmlFor="ethnicity">
                            Ethnicity
                            <select
                            name="ethnicity"
                            value={ethnicities}
                            onChange={(e) => {
                                setEthnicities(e.target.value);
                            }}  
                            onBlur={(e) => {
                                setEthnicities(e.target.value);
                            }} // handles when drop down is clicked off of. 
                            >       
                            <option /> {/**Gives us a default empty option*/}
                                    {ETHNICITIES.map((ethnicities) => (
                                        <option key={ethnicities} value={ethnicities}>
                                            {ethnicities}
                                        </option>
                                    ))};
                            </select>
                        </label>
                        <label htmlFor="gender">
                            Gender
                            <select
                            name="gender"
                            value={gender}
                            onChange={(e) => {
                                setGender(e.target.value);
                            }}  
                            onBlur={(e) => {
                                setGender(e.target.value);
                            }} // handles when drop down is clicked off of. 
                            >       
                            <option /> 
                            {/**Gives us a default empty option*/}
                                    {GENDER.map((gender) => ( // gender is each item within the GENDER array. Map gives us individual items. 
                                        <option key={gender} value={gender}>
                                            {gender}
                                        </option>
                                    ))};
                            </select>
                        </label>
                        <label htmlFor="occupation">
                            Occupation 
                            <input
                            type="text" 
                            name="occupation" 
                            value={occupation} 
                            onChange={(e) => setOccupation(e.target.value)} 
                            />
                        </label>
                        <button>Submit</button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default SearchParams;

