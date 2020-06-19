import React, { Component } from 'react'
import Page from './page'
import { connect } from 'react-redux'
import  { userLoginFetch }  from '../../redux/actions/loginUser'
import validateInput from '../../Helpers/login'


class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            errors: {},
            errorState: false,
            username: "",
            password: "",
            isLoading: false
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    

    handleChange = event => {
        this.setState({[event.target.name]: event.target.value });
        // this.setState({username});
        // this.setState({password});
    }

    isValid() {
        const { errors, isValid } =validateInput(this.state);
        if (!isValid) {
            this.setState({errorState: true});
            this.setState({ errors });
        }
        else {
            this.setState({errorState: false});
        }
        return isValid;
    }

    handleSubmit = event => {
        event.preventDefault()
        if (this.isValid()){
            this.setState({errors: {}, isLoading: true, errorState:false});
            this.props.userLoginFetch(this.state);

        } 
        // this.props.userLoginFetch(this.state)
      }

    render() {
        const { username, password, errors, isLoading, errorState } = this.state;
        return (
            <Page 
            username={username}
            passw={password}
            errors={errors}
            handleChange={this.handleChange}
            handleSubmit={this.handleSubmit}
            isLoading={isLoading}
            errorState={errorState}/>
        );
    }

}

// Login.prototype = {
//     userLoginFetch: React.prototype.func.is
        
// }


// const mapDispatchToProps = dispatch => ({
//     userLoginFetch: userInfo => dispatch(userLoginFetch(userInfo))

// });

export default connect(null, userLoginFetch)(Login);
// export default connect(null, mapDispatchToProps)(Login);

// export default Login;