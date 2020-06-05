import React, { Component } from "react";
import {Col, ProgressBar, Form, Button} from 'react-bootstrap';
import { render } from "@testing-library/react";
// import Users  from "./Users";

class RegisterPlant extends Component  {
    constructor (props) {
        super(props)  

    }
  
    render(){
        return(
            <Form>
                <Form.Group controlId="formBasicEmail">
                   <Form.Label>Email address</Form.Label>
                   <Form.Control type="email" placeholder="Enter email" />
                   <Form.Text className="text-muted">
                     We'll never share your email with anyone else.
                   </Form.Text>
                 </Form.Group>

                 <Form.Group controlId="formBasicPassword">
                   <Form.Label>Password</Form.Label>
                   <Form.Control type="password" placeholder="Password" />
                 </Form.Group>
                 <Form.Group controlId="formBasicCheckbox">
                   <Form.Check type="checkbox" label="Check me out" />
                 </Form.Group>
                 <Button variant="primary" type="submit">
                   Submit
                 </Button>

            </Form>
        )
    }
}


export default RegisterPlant