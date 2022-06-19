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
import mob from "./pic/mob.jpg"
import TextField from '@mui/material/TextField';
import { Container, Grid } from '@material-ui/core';
import {
  TwitterIcon,
  TwitterShareButton,
} from "react-share"

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

export default function FromTweet(){
    return(
        <div>
           <Box sx = {{height:100 }}></Box>
           <Box sx={{ bgcolor: '#ffffff', width: 900,  borderRadius: '16px'}}>
           <Container maxWidth="sm" >
           <Box sx = {{height:50 }}></Box>
            <h2>Tweetから生成</h2>
            <GetId />
            <Box sx = {{height:150 }}></Box>
            </Container >
            </Box>
            <Box sx = {{height:50 }}></Box>
            <Box sx={{ bgcolor: '#ffffff', width: 900,  borderRadius: '16px'}}>
            <Container maxWidth="sm">
              
            <Box sx = {{height:50 }}></Box>
            <h2>シェアする</h2>
            <Box sx = {{height:50 }}></Box>

            <TwitterShareButton
              url={"https://twitter.com"}
              title={"wawawa"}
              hashtags={"推しジェネ"}
            >
              <TwitterIcon size={50} round />
            </TwitterShareButton>
            <Box sx = {{height:100 }}></Box>
            </Container >
            </Box>
            <Box sx = {{height:100 }}></Box>
        </div>
    )
  }
  
  function GetId(){
    return(
      <Grid container alignItems="center" justify="center">
        <form>
            <Box sx = {{width:"100%", display: 'flex',
          alignItems: 'center',
          flexDirection: 'row',}}>
            <TextField id="outlined-basic" label="@username" variant="outlined" margin='none'/>
            <Box sx = {{width:20 }}></Box>
            <Button Button variant="contained" color="secondary" size = "large" >生成</Button>
            </Box>
        </form>
        <Box sx = {{height:150 }}></Box>
        <img src= {mob} alt="picture" width = "700"/>
      </Grid>
    );
  }