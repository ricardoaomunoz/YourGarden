import Axios from 'axios';

const TOKEN_KEY = 'GROWINGCLUB_TOKEN';

export function setToken(token) {
    localStorage.setItem(TOKEN_KEY, token)
}

export function getToken() {
    return localStorage.getItem(TOKEN_KEY);
}

export function deleteToken() {
    localStorage.removeItem(TOKEN_KEY);
}

// Si existe un token el se lo va a agregar al header http autorizacion 
// para que el servidor reconozca quien es el usuario
export function initAxiosInterceptors() {
    Axios.interceptors.request.use(function(config) {
        const token = getToken();

        if (token){
            config.headers.Authorization = `bearer ${token}`;
        }
        return config;
        
    });
    Axios.interceptors.response.use(
        function(response) {
            return response;
        },
        function(error) {
            // if(error.response.status === 401)
            console.log(error);
            console.log(error.response.status);
            
        }
    )
    
}