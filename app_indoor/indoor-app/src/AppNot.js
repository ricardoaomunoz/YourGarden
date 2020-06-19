import React, { useState, useEffect } from 'react'
import httpClient from './fetch-client'
import SignIn from './SignIn'
import { setToken, deleteToken, getToken, initAxiosInterceptors } from './Helpers/auth-helper'
import {userLoginFetch} from '../'

initAxiosInterceptors();

export default function App() {
    const [user, setUser] = useState(null);
    const [userState, setUserState] = useState(true);

    useEffect( () => {
        async function userExist() {
            // Primero mirar si existe un token 
            // let gettoken = false;
            if(!getToken()) {
                setUserState(false);
                return;
            }
            try {
                const { data: usuario } = await httpClient.get('user/status'); 
            } catch (error) {
                console.log(error)
                
            }
        }
        userExist();
    }, []);

    async function login(username, password) {
        console.log("function login")

        const  data  = await httpClient.post(`user/login`, {
            username,
            password
        });
        if(!data.ok){
            console.log('some error')
        }
        else{
            // const login_data = data.json();
            console.log(data.json());
            console.log(data.auth_token);

        }
        
        
        // setUser(data.user);
    }
    return (
        <>
        <SignIn 
        login={login} />
        
        <div>{JSON.stringify(user)}</div>
        </>
    );
}