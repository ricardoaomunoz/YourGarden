import React, { Component } from "react";
import {Col, Button} from 'react-bootstrap';
import { render } from "@testing-library/react";
import SetTimer from './SetTimer'
// import Users  from "./Users";

class TimeSetter extends Component  {
    constructor (props) {
        super(props)
        this.state={
            showMo: false,
            handleClose : () => this.setState({showMo: false}),
            handleShow : () => this.setState({showMo: true}),
            
        }
        this.TimeSubmit = this.TimeSubmit.bind(this)


    }
    TimeSubmit (timerSent) {
        console.log("Aqui se envio desde el prop timeSent")
        this.props.setTime(timerSent)

    }
    render(){
        const {showMo, handleClose, handleShow} = this.state
        const {turnOn, turnOff, automatic} = this.props
        
        
    return(
        <Col>
            <h2>Timer for Light</h2>
            <div className='custom-control custom-switch'>
                <input
                  type='checkbox'
                  className='custom-control-input'
                  id='customSwitchesChecked'
                  checked = {automatic}
                />
                <label className='custom-control-label' htmlFor='customSwitchesChecked'>
                </label>
            </div>
            <p>
                The time setter to turn on the light is: <b>{turnOn}
                </b> And the time setter to turn off the light is: <b> {turnOff} 
                </b>
            </p> 
            <Button variant="primary" size="lg" onClick={handleShow} active>Change Time</Button>
            <SetTimer
                turnOn={turnOn}
                turnOff={turnOff}
                showMo={showMo}
                handleClose={handleClose}
                TimeSubmit={this.TimeSubmit}
                />
        </Col>
    )
}
    // const context = useContext(TimerSets);
}

export default TimeSetter