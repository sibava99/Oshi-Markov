import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Box from '@mui/material/Box';
import ArticleIcon from '@material-ui/icons/Assignment';
import { Link } from 'react-router-dom';
import lome from "./pic/lome.jpg"
import { Grid } from '@material-ui/core';
import Container from '@mui/material/Container';
import TwitterIcon from '@material-ui/icons/Twitter';

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
        <Box sx = {{height:100}}></Box>
        <Box sx={{ bgcolor: '#ffffff', width: 900,  borderRadius: '16px'}}>
        <Box sx = {{height:100}}></Box>
        <Salome />
        </Box>
        <Box sx = {{height:50}}></Box>
        <Box sx={{ bgcolor: '#ffffff', width: 900,  borderRadius: '16px'}}>
        <Chalenge />
        </Box>
        <Box sx = {{height:50}}></Box>
        </div>
    );
}

function Salome(){
    return(
        <div align = "center">
            <img src= {lome} alt="picture" width = "700"/>
            <Box sx = {{height:50}}></Box>
            <Button variant="contained" color="secondary" size = "large" >生成</Button>
            <Box sx = {{height:50}}></Box>
        </div>
    );
}

function Chalenge(){
    return(
        <div>
            <Container maxWidth="sm" >
              
            <Box sx = {{height:50}}></Box>
                <h2>やってみよう！</h2>
                <Box sx = {{height:50 , borderTop:2, borderColor:"#f20d99"}}></Box>
                <p>TwiterIDまたはテキストデータからマルコフ連鎖で推し語録を生成しよう！</p>
                <Box sx = {{height:50 }}></Box>
                <Grid container spacing={2}>
                  <Grid item xs = {6}><Button variant="contained" color="secondary" size = "large" component={Link} to = "/fromTweet" startIcon={<TwitterIcon/>}>Tweetから生成</Button></Grid>
                  <Grid item xs = {6}><Button variant="contained" color="inherit" size = "large" component={Link} to = "/fromCopus" startIcon={<ArticleIcon />}>Copusから生成</Button></Grid>
                </Grid>
                
                <Box sx = {{height:50}}></Box>
            </Container>
        </div>
    );
}