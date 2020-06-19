import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Title from './Title'
import { Table, TableHead, TableCell, TableRow, TableBody, Link } from '@material-ui/core';



function preventDefault(event) {
    event.preventDefault();
  }

const useStyles = makeStyles((theme) => ({
    seeMore: {
      marginTop: theme.spacing(3),
    },
  }));

export default function ShowPlnats(){
    const classes = useStyles();
    return (
        <React.Fragment>
            <Title> Plants </Title>
            <Table size="small">
                <TableHead>
                  <TableRow>
                    <TableCell>Imagen</TableCell>
                    <TableCell>Last UpDate</TableCell>
                    <TableCell>Nick NAme</TableCell>
                    <TableCell>Grow</TableCell>
                    <TableCell>Comment</TableCell>
                    <TableCell>Extra Data</TableCell>
                    <TableCell align="right">Stage</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>

                </TableBody>
                </Table>
                <div className={classes.seeMore}>
                    <Link color="primary" href="#" onClick={preventDefault}>
                      See all your plants
                    </Link>
                </div>   
        </React.Fragment>
    )
    
}