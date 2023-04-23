import React, { useState, useEffect } from 'react';
import axios from "axios";
import './Myapp.css';

function MeasurementForm() {
    const [height, setHeight] = useState('');
    const [weight, setWeight] = useState('');
    const [age, setAge] = useState('');
    const [waist, setWaist] = useState('');
  
    const [showWaistInput, setShowWaistInput] = useState(false);
  
    const handleSubmit = async (event) => {
      event.preventDefault();
      
        const response = await axios.post('http://127.0.0.1:8000/get_measurement', {
          height,
          weight,
          age,
        }).catch(function (error){
          setWaist('');
          alert("Plz Add the Waist Value First.");
          setShowWaistInput(true);
        });
          if (response.status === 200) {
            setWaist(response.data.waist);
            setShowWaistInput(false);
          }    
      }; 
  
    const handleSetMeasurement = async (event) => {
      event.preventDefault();
      setShowWaistInput(true);
    };
  
    const handleWaistSubmit = async (event) => {
      event.preventDefault();
      try {
        const response = await axios.post('http://127.0.0.1:8000/set_measurement', {
          height,
          weight,
          age,
          waist,
        });
        if (response.status !== 200) {
          throw new Error('Error setting measurement');
        }
        setShowWaistInput(false);
      } catch (error) {
        console.error(error);
        alert(error.message);
      }
    };

    return (
        <div >
          <div className="form-container">
            <div className='title'><h2>Waist Size Calculator</h2></div>
            <form onSubmit={handleSubmit}>
              <label>
                Height:
                <input type="text" placeholder='Enter height in cms.' value={height} onChange={(event) => setHeight(event.target.value)} />
              </label>
              <label>
                Weight:
                <input type="text" placeholder='Enter weight in kgs.' value={weight} onChange={(event) => setWeight(event.target.value)} />
              </label>
              <label>
                Age:
                <input type="text" placeholder='Enter age in years.' value={age} onChange={(event) => setAge(event.target.value)} />
              </label>
              <button type="submit">Submit</button>
            </form>
            {waist && <p>Your waist measurement is {waist} cm.</p>}
          </div>
          {!showWaistInput && <button className="add-measurement-button" onClick={handleSetMeasurement}>Add my measurement</button>}
          {showWaistInput && (
            <div className="form-container">
              <form onSubmit={handleWaistSubmit}>
                <label>
                  Waist:
                  <input type="text" value={waist} onChange={(event) => setWaist(event.target.value)} />
                </label>
                <button type="submit">Submit</button>
              </form>
            </div>
          )}
        </div>
      );
          }
      
export default MeasurementForm;