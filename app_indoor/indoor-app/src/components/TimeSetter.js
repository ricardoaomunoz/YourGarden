import React from "react";
import { makeStyles, Typography, Link } from "@material-ui/core";
import Title from './Title'
// import Users  from "./Users";

function preventDefault(event) {
    event.preventDefault();
  }

const useStyles = makeStyles({
    timerContext: {
        flex: 1,
    },
});

export default function TimeSetter(props){
    const classes = useStyles();        
    
    return(
        <React.Fragment>
            <Title>Time Light</Title>
            <Title>Time Light </Title>
            <Typography variant="h5" color="initial" component="p">
                Time to Light On: <b> {props.turnOn} </b>
            </Typography>
            <Typography variant="h5" color="initial" component="p">
                Time to Light Off: <b> {props.turnOff} </b>
            </Typography>
            <Typography color="textSecondary" className={classes.depositContext}>
              <br></br>
            </Typography>
            <div>
                <Link color="primary" href="#" onClick={preventDefault}>
                  Set Time
                </Link>
            </div>

        </React.Fragment>


        // <Col>
        //     <h2>Timer for Light</h2>
        //     <div className='custom-control custom-switch'>
        //         <input
        //           type='checkbox'
        //           className='custom-control-input'
        //           id='customSwitchesChecked'
        //           checked = {automatic}
        //         />
        //         <label className='custom-control-label' htmlFor='customSwitchesChecked'>
        //         </label>
        //     </div>
        //     <p>
        //         The time setter to turn on the light is: <b>{turnOn}
        //         </b> And the time setter to turn off the light is: <b> {turnOff} 
        //         </b>
        //     </p> 
        //     <Button variant="primary" size="lg" onClick={handleShow} active>Change Time</Button>
        //     <SetTimer
        //         turnOn={turnOn}
        //         turnOff={turnOff}
        //         showMo={showMo}
        //         handleClose={handleClose}
        //         TimeSubmit={this.TimeSubmit}
        //         />
        // </Col>
    );

    // const context = useContext(TimerSets);
}

