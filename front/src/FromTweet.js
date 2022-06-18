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
import TextField from '@mui/material/TextField';

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
            <h2>Tweetから生成</h2>
            <GetId />
            <h2>シェアする</h2>
        </div>
    )
  }
  
  function GetId(){
    return(
        <form>
            <TextField id="outlined-basic" label="@username" variant="outlined" margin='none'/> <Button color="inherit" >生成</Button>
        </form>
    );
  }