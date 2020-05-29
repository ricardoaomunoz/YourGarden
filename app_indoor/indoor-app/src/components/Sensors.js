import React, { Component } from "react";
import {Col, ProgressBar} from 'react-bootstrap';
import { render } from "@testing-library/react";
// import Users  from "./Users";

class Sensors extends Component  {
    constructor (props) {
        super(props)  


    }
  
    render(){
        const {temperature, humidity} = this.props
        let variant = "info"
        if (temperature <= 0){
            variant = "danger"
        } else{
            variant ="success"
        }
        
        
        
    return(
        <Col>
            <h2>Sensors</h2>
            <h3>Temperature and Humidity</h3>
            <p>Temperature:</p>
            <div>
                <ProgressBar animated now={temperature} variant={variant} label={`${temperature} °C `}/>
               
            </div>
            <p>Humidity:</p>
            <div>
                <ProgressBar animated now={humidity} variant="info" label={`${humidity} %`}/>
               
            </div>
            
        </Col>
            
    )
}
    // const context = useContext(TimerSets);
}

export default Sensors