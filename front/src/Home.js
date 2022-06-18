import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Box from '@mui/material/Box';
import { Link } from 'react-router-dom';
import lome from "./pic/lome.jpg"
import { Grid } from '@material-ui/core';
import Container from '@mui/material/Container';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

export default function Home() {
    const classes = useStyles();
    return(
        <div>
        <Salome />
        <Chalenge />
        </div>
    );
}

function Salome(){
    return(
        <div align = "center">
            <img src= {lome} alt="picture" width = "50%"/>
            <br></br>
            <Button color="inherit" >生成</Button>
        </div>
    );
}

function Chalenge(){
    return(
        <div>
            
            <Container maxWidth="sm" color="secondary">
            <h2>やってみよう！</h2>
            <Grid container spacing={2}>
              <Grid item xs = {6}><Button variant="contained" color="secondary" size = "large" component={Link} to = "/fromTweet">Tweetから生成</Button></Grid>
              <Grid item xs = {6}><Button variant="contained" color="inherit" size = "large" component={Link} to = "/fromCopus">Copusから生成</Button></Grid>
              
            </Grid>
            </Container>
            
        </div>
    );
}