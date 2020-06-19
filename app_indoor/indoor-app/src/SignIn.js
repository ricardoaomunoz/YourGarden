// import React, { useState} from 'react';
// import { Typography, Link, CssBaseline, Avatar, Checkbox, Box } from '@material-ui/core/'
// import { makeStyles, Container, TextField,  FormControlLabel, Button, Grid } from '@material-ui/core';
// import LockOutlinedIcon from '@material-ui/icons/LockOutlined';

// function Copyright() {
//     return (
//         <Typography variant="body" color="textSecondary" align="center">
//             {'Copyright © '}
//             <Link color="inherit" href="https://material-ui.com/">
//                 GrowingClub
//             </Link>{' '}
//             {new Date().getFullYear()}
//             {'.'}
//         </Typography>
//     );
// }


// const useStyles = makeStyles((theme) => ({
//     paper: {
//         marginTop: theme.spacing(8),
//         display: 'flex',
//         flexDirection: 'column',
//         alignItems: 'center',
//       },
//       avatar: {
//         margin: theme.spacing(1),
//         backgroundColor: theme.palette.secondary.main,
//       },
//       form: {
//         width: '100%', // Fix IE 11 issue.
//         marginTop: theme.spacing(1),
//       },
//       submit: {
//         margin: theme.spacing(3, 0, 2),
//       },
    
    

// }));


// export default function SignIn(props) {
//     const [userName, setUserName] = useState(null);
//     const [password, setPassword] = useState(null);


//     const sendLoginInfo = (event) => {
//         // console.log(`
//         // usernamr: ${userName}
//         // password: ${password}`
//         // );
//         props.login(userName, password);
//         event.preventDefault();
        
//         // console.log("click");
        
//     }


//     // useEffect(() => {
//     //     async function uploadUser(){
//     //         if (!getToken()) {
//     //             setisUSer(false);
//     //             return;
//     //         }
//     //         try {
//     //             const { data: usuario } = await Axios.get('/api/user/status')
//     //         } catch (error) {
//     //             console.log(error);
//     //             // mostrar error de conexion
//     //         }
//     //     }
//     // });

//     // async function login(username, password) {
//     //     const { data } = await Axios.post('/api/user/login', {
//     //         username,
//     //         password
//     //     });
//     //     setUsuario(data.usuario);

//     // }
//     const classes = useStyles();

//     return(
//         <Container componenet="main" maxWidth="xs">
//             <CssBaseline />
//             <div className={classes.paper}>
//                 <Avatar className={classes.avatar}>
//                     <LockOutlinedIcon />
//                 </Avatar>
//                 <Typography variant="h1" variant="h5">
//                     Sign in 
//                 </Typography>
//                 <form onSubmit={sendLoginInfo} className={classes.form}  noValidate>
//                     <TextField
//                       id="email_signin"
//                       variant="outlined"
//                       margin="normal"
//                       required
//                       fullWidth
//                       id="email"
//                       label="Username/Email Address"
//                       name="email"
//                       autoComplete="email"
//                       autoFocus
//                       onChange={ (ev)=> setUserName(ev.target.value) }
//                     //   value={}
//                     //   onChange={}
//                     />
//                     <TextField
//                       variant="outlined"
//                       margin="normal"
//                       required
//                       fullWidth
//                       name="password"
//                       label="Password"
//                       type="password"
//                       id="password"
//                       autoComplete="current-password"
//                       onChange={ (ev)=> setPassword(ev.target.value) }
//                     />
//                     <FormControlLabel
//                       control={<Checkbox value="remember" color="primary" />}
//                       label = "Remember Me"
//                     />
                    
//                     <Button
//                       type="submit"
//                       fullWidth
//                       variant="contained"
//                       color="primary"
//                       className={classes.submit}
//                       onClick= {()=> console.log('click on clik')}
//                     >
//                       Sign In
//                     </Button>
//                     <Grid container >
//                         <Grid item xs>
//                             <Link href="#" variant="body2">
//                                 Forgot password?
//                             </Link>
//                         </Grid>
//                     </Grid>
//                 </form>
//             </div>
//           <Box mt={8}>
//               <Copyright />
//           </Box>
//         </Container>
//     );
// }