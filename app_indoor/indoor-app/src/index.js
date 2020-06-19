import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom';
import Login from './components/login/index'
import user from './redux/users'


const Root = (
  <Provider store={user}>
    <BrowserRouter>
      <Switch>
        <Route path="/login" component={Login}></Route>
        <Redirect from="/" to="/login" />
      </Switch>
    </BrowserRouter>
  </Provider>

)
ReactDOM.render(Root, document.getElementById('root'));

