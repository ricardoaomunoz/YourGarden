import React, { Component, useState } from 'react';
import io from 'socket.io-client'
import logo from './logo.svg';
import {Container, Row, Col, Navbar, Nav, Image} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'
import './App.css';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import  { Timer }  from './components/SetTimer';
import { NoMatch } from './NoMatch';
import { render } from '@testing-library/react';
import { ThemeContext } from 'styled-components';
// import header_img from './components/images/header_img.jpg'
import Home from './components/Home'
import TimeSetter from './components/TimeSetter'
import Carousel from './components/CarouselImg'
import Sensors from './components/Sensors'

const username = prompt("What is your username");

// const socket = io("http://localhost:5010", {
//   transports: ["websocket", "polling"]
// });

let endPoint = "http://192.168.1.99:5000";
let socket = io.connect(`${endPoint}`);
export const TimerSets = React.createContext();
console.log("io connected");

class App extends Component{
  

  constructor(props) {
    super(props);
    this.state = {
      userName: username,
      automatic: true,
      turnOn: "",
      turnOff: "",
      users: [],
      temperature: -10,
      humidity: 20
    }
    this.setTime = this.setTime.bind(this)
  }

  setTime (timeLight){
    socket.emit('time-light', {timer: timeLight})
  }

    // socket.on('connect', ()=> {
    //   console.log("Conectado %s ####", username);
    //   socket.emit("username", username)
    // });
  setSocketListeners () {
    socket.on('retrieve_active_users', () => {
      console.log("retrieve username");
      console.log(this.state.userName)
      if (this.state.userName) {
        socket.emit('activate_user', { username: this.state.userName })
      }
    })

      // llega solo uno
    // socket.on("connected", user => {
    //   // console.log(user);
    //   // console.log(this.state.users);
    //   const {users} = this.state
    //   this.setState({ users: [...users, user] });
    // })

    socket.on('time_setter', (data) => {
      const timeOn = data['turn_on']
      const timeOff = data['turn_off']
      const { turnOn, turnOff } = this.state
      this.setState({turnOn: timeOn, turnOff: timeOff})
    })

    socket.on('user_activated', (data) => {
      const user = data['user']
      const { users } = this.state
      if (users.indexOf(user) === -1 ) {
        this.setState({ users: [...users, user] });
      }
    })

    socket.on('sensor1_setter', (data) => {
      console.log("temp data")
      console.log(data)
      const temp = data['temperature']
      const humd = data['humidity']
      const {temperature, humidity} = this.state
      this.setState({ temperature: temp, humidity: humd})
    })
  }
    // llegan todos
    // socket.on("users", userss => {
    //   const {users} = this.state
    //   // console.log(userss);
    //   // console.log(this.state.users);
    //   this.setState({users: userss});
    //   console.log(users);

    // });


    componentDidMount () {
      this.setSocketListeners()
    }


    render(){
      const {userName, users, turnOn, turnOff, automatic, temperature, humidity} = this.state
      return (
        <Container className='App'>
          <Row className="justify-content-md-center">
            <Col>
              <Navbar bg="primary" varinat="dark">
                <Navbar.Brand href=""> IndoorCLub </Navbar.Brand>
                <Nav className="ml-auto">
                  <Nav.Link href="">Home</Nav.Link>
                  {/* <Nav.Link href={Timer}>Timer</Nav.Link> */}
                </Nav>
              </Navbar>
            </Col>
          </Row>
          <Row className="justify-content-md-center">
            <Col>
              <Carousel />
              {/* <Image src={header_img} fluid /> */}
            </Col>
          </Row>
          <Row className="justify-content-md-center">
            <Col>
              <Home
                userName={userName}
                users={users}/>
            </Col>
          </Row>
          <Row>
            <TimeSetter 
              turnOff= {turnOff}
              turnOn= {turnOn}
              automatic = {automatic}
              setTime={this.setTime}
            />
            <Sensors 
              temperature={temperature}
              humidity={humidity}
              />
          </Row>
          <br></br>
          <br></br>
          <br></br>
        </Container>

      

      // <React.Fragment>
      //   {/* <tbody>
      //     {this.state.users.map((name, id) => {
      //       return(
      //         <li key={id}>{name}</li>
      //       )
      //     })}
        
      //   </tbody> */}
      //   <td>Hello {username}</td>
      //   {/* <td>
      //     <ul id="users">
      //       {this.state.users.map(({ name, id }) => (
      //         <li key={id}>{name}</li>
      //       ))}
      //     </ul>
      //   </td> */}
      //   <Router>
      //     <Switch>
      //       <TimerSets.Provider value={this}>
      //         <Route exact path="/" component={Timer} /> 
      //       </TimerSets.Provider>
      //       <Route component={NoMatch} />
      //     </Switch>
      //   </Router>  
      // </React.Fragment>
      
    );
  }
}

// const mapDispatchToProps = {
//   updateTotalMarketCap
// };

// export const SocketManager = connect(
//   null,
//   // mapDispatchToProps
// )(App);

// export default SocketManager;

export default App;



// import React, { useState, useEffect } from "react";
// import io from "socket.io-client";

// let endPoint = "http://localhost:5000";
// let socket = io.connect(`${endPoint}`);

// const App = () => {
//   const [messages, setMessages] = useState(["Hello And Welcome"]);
//   const [message, setMessage] = useState("");

//   useEffect(() => {
//     getMessages();
//   }, [messages.length]);

//   const getMessages = () => {
//     socket.on("message", msg => {
//       //   let allMessages = messages;
//       //   allMessages.push(msg);
//       //   setMessages(allMessages);
//       setMessages([...messages, msg]);
//     });
//   };

//   // On Change
//   const onChange = e => {
//     setMessage(e.target.value);
//   };

//   // On Click
//   const onClick = () => {
//     if (message !== "") {
//       socket.emit("message", message);
//       setMessage("");
//     } else {
//       alert("Please Add A Message");
//     }
//   };

//   return (
//     <div>
//       {messages.length > 0 &&
//         messages.map(msg => (
//           <div>
//             <p>{msg}</p>
//           </div>
//         ))}
//       <input value={message} name="message" onChange={e => onChange(e)} />
//       <button onClick={() => onClick()}>Send Message</button>
//     </div>
//   );
// };

// export default App;
