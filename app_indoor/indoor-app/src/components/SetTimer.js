import React, { Component} from "react";
import {Modal, Form, Button} from 'react-bootstrap';
import {TimerSets} from '../App'
import PropTypes from 'prop-types'

class SetTimer extends Component  {
    constructor (props) {
        super(props)
       this.submit = this.submit.bind(this)
    }

    submit(event){
        event.preventDefault();
        let msg = [event.target.TimeOn.value, event.target.TimeOff.value];
        // alert(msg);
        this.props.TimeSubmit(msg);
        this.props.handleClose();
    }

    render(){
        const {showMo, handleClose, turnOn, turnOff} = this.props
        
        
    return(
        <Modal show={showMo} onHide={handleClose}>
            <Modal.Header closeButton>
              <Modal.Title>Set Timer</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form onSubmit={this.submit} id="timeform">
                    <Form.Group controlId="FormSetOnTimer">
                        <Form.Label>Set Light On</Form.Label>
                        <Form.Control type="time" name="TimeOn" defaultValue={turnOn} placeholder="Set time"/>
                    </Form.Group>
                    <Form.Group controlId="FormSetOffTimer">
                        <Form.Label>Set Light Off</Form.Label>
                        <Form.Control type="time" name="TimeOff" defaultValue={turnOff} placeholder="Set time"/>
                    </Form.Group>
                    <Button variant="primary" type="submit">submit</Button>
                </Form>    
            </Modal.Body>
           
            <Modal.Footer>
              <Button variant="secondary" onClick={handleClose}>
                Close
              </Button>
              {/* <Button variant="primary" onClick={handleClose}>
                Save Changes
              </Button> */}
            </Modal.Footer>
        </Modal>
    )
}
    // const context = useContext(TimerSets);
}

export default SetTimer
