
import { createStore, combineReducers } from 'redux';
import user from './reducers/user'

const reducer = combineReducers({
    user,
});

const users = createStore(reducer);

export default users;