import { useState } from "react"; 

const SearchParams = () => {
    /*
    onst [inputs, setInputs] = useState({
        username: '',
        age: '',
        profession: ''
    });*/
    const ETHNICITIES = ["Black", "White", "Asian", "Middle Eastern", "Indigenous"];
    const GENDER = ["Male", "Female", "Non-binary", "Other"];
    const [age, setAge] = useState(0); 
    const [username, setUsername] = useState("");  
    const [ethnicities, setEthnicities] = useState("");  
    const [gender, setGender] = useState("");
    const [occupation, setOccupation] = useState(); 

    // manages state of input
    const handleChange = (event) => { 
        const name = event.target.name; // this updates the computed [name] property, giving it the name of whatever the name of input is. 
        const value = event.target.value; // updates the value when user types
        setInputs(values => ({...values, [name]: value}))
    }

    const handleSubmit = (event) => {
        event.preventDefault(); // default action is a page reload via submit, don't want that. 
        console.log(inputs); // sends the state of our inputs to console for handling. 
    }

    return (
        <div className="search-params">
            <form onSubmit={handleSubmit}>
                <label htmlFor="userName">
                    Please enter username: 
                    <input
                    type="text" 
                    name="userName" 
                    value={username} 
                    placeholder="Username" 
                    onChange={(e) => setUsername(e.target.value)} 
                    />
                </label>
                <label htmlFor="age">
                    Please enter your age: 
                    <input
                    type="number"
                    name="age"
                    value={age}
                    placeholder="Age"
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
                    placeholder="occupation" 
                    onChange={(e) => setOccupation(e.target.value)} 
                    />
                </label>
                <button>Submit</button>
            </form>
        </div>
    );
};

export default SearchParams;

