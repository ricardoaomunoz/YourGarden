import React, { Component } from "react";
import {Jumbotron, Container} from 'react-bootstrap';
import { render } from "@testing-library/react";
// import Users  from "./Users";

class Home extends Component  {
    constructor (props) {
        super(props)

    }
    render(){
        const {userName, users} = this.props
        console.log("home component");
        console.log(users);
        const usersList = users.map((name, i) => {
            console.log(name);
            console.log(i);
            return (
                <p><strong>{i}: </strong>{name}</p>
            )
        })
        return(
            
            <Jumbotron>
                <h2>Welcome {userName} to Indoor Club </h2>
                <p>The science of the sowing....</p>
                {usersList}
            </Jumbotron>
                     
        )}
    // const context = useContext(TimerSets);
}

export default Home



// export const Home = ()=> {
//     // const context = useContext(TimerSets);
//     const [userName, setuserName] = useState("");
//     const [users, setusers] = useState([]);

//     return(
//     <div>
//         <Container>
//             <Jumbotron>
//                 <h2>Wlcome {userName} to Indoor Club </h2>
//                 <p>The science of the science of sowing....</p>
//                 <tbody>
//                     {users.map((name, id) => {
//                       return(
//                         <li key={id}>{name}</li>
//                       )
//                     })}
//                 </tbody>
//             </Jumbotron>
//             <Alert.Link href="/about">
//                 <Button bsStyle="primary">About</Button>
//             </Alert.Link>
            
//         </Container>
        
//     </div>
//     )
    
// }