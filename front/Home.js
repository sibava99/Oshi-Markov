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
            <h2>Home</h2>
            <Button color="inherit" >生成</Button>
        </div>
    );
}

function Chalenge(){
    return(
        <div>
            <h2>やってみよう！</h2>
            <Button color="inherit" component={Link} to = "/fromTweet">Tweetから生成</Button><Button color="inherit" component={Link} to = "/fromCopus">Copusから生成</Button>
        </div>
    );
}