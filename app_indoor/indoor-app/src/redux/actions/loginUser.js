const urlBase = 'http://localhost:5000/api'

/**
 * @param {string}  url url a la cual consultar
 * esta funcion detecta si es una nueva url base (comienza con http:// o https://).
 * en caso de ser asi, retorna la url. en caso contrario, se asume que es un fragmento
 * de path por lo que se concatena con la constante urlBase
 **/
const readUrl = (url = '') =>
  url.startsWith('http://') || url.startsWith('https://') ? url : `${urlBase}/${url}`

  
// const userLoginFetch = user => {
//     return dispatch => {
//       return fetch(readUrl('user/login'), {
//         method: "POST",
//         headers: {
//           'Contect-Type': 'application/json',
//           Accept: 'application/json'
//         },
//         body: JSON.stringify({user})
//       })
//       .then(resp => resp.json())
//       .then(data => {
//         if (data.message) {
//           console.log("error");
//           console.log(data.message);
//         } else {
//           localStorage.setItem("token", data.token_auth)
//           dispatch(loginUser(data.user))
//         }
//       })
//     }
//   }

function userLoginFetch(data) {
  return fetch(readUrl('user/login'), {
    method: "POST",
    headers: {
      'Contect-Type': 'application/json',
      Accept: 'application/json'
    },
    body: JSON.stringify({data})
  })
  
}
// const loginUser = userObj => ({
//     type: 'LOGIN_USER',
//     payload: userObj,
//   })

  
export default userLoginFetch;