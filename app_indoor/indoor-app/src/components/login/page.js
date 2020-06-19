import React from 'react';
import { Typography, Link, CssBaseline, Avatar, Checkbox, Box } from '@material-ui/core/'
import { makeStyles, Container, TextField,  FormControlLabel, Button, Grid } from '@material-ui/core';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';

function Copyright() {
    return (
        <Typography variant="body" color="textSecondary" align="center">
            {'Copyright © '}
            <Link color="inherit" href="https://material-ui.com/">
                GrowingClub
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}


const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      },
      avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
      },
      form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(1),
      },
      submit: {
        margin: theme.spacing(3, 0, 2),
      },
    
    

}));


export default function SignIn(props) {
    // const [userName, setUserName] = useState(null);
    // const [password, setPassword] = useState(null);
    const {
        username,
        passw,
        errors,
        handleSubmit,
        handleChange,
        isLoading,
        errorState,
    } = props;


    // const sendLoginInfo = (event) => {
    //     // props.login(userName, password);
    //     // event.preventDefault();
    //     console.log(userName);
    //     console.log(password);
    //     console.log("click");
        
    // }

    const classes = useStyles();

    return(
        <Container componenet="main" maxWidth="xs">
            <CssBaseline />
            <div className={classes.paper}>
                <Avatar className={classes.avatar}>
                    <LockOutlinedIcon />
                </Avatar>
                <Typography component="h1" variant="h5">
                    Sign in 
                </Typography>
                <form onSubmit={handleSubmit} className={classes.form}  noValidate>
                    <TextField
                      variant="outlined"
                      margin="normal"
                      required
                      fullWidth
                      id="username"
                      label="Username/Email Address"
                      name="username"
                      autoComplete="email"
                      autoFocus
                      value = {username}
                      onChange={handleChange}
                      helperText={errors.username}
                      error={errorState}
                    />
                    <TextField
                      variant="outlined"
                      margin="normal"
                      required
                      fullWidth
                      name="password"
                      label="Password"
                      type="password"
                      id="password"
                      autoComplete="current-password"
                      value = {passw}
                      onChange={handleChange }
                      helperText={errors.password}
                      error={errorState}
                    />
                    <FormControlLabel
                      control={<Checkbox value="remember" color="primary" />}
                      label = "Remember Me"
                    />
                    
                    <Button
                      type="submit"
                      disabled={isLoading}
                      fullWidth
                      variant="contained"
                      color="primary"
                      className={classes.submit}
                    //   onClick= {()=> console.log('click on clik')}
                    >
                      Sign In
                    </Button>
                    <Grid container >
                        <Grid item xs>
                            <Link href="#" variant="body2">
                                Forgot password?
                            </Link>
                        </Grid>
                    </Grid>
                </form>
            </div>
          <Box mt={8}>
              <Copyright />
          </Box>
        </Container>
    );
}