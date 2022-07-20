import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Box from '@mui/material/Box';
import logo from "./pic/logo.png"
import { Link } from 'react-router-dom';
import style from './Header.css'

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

export default function Header() {
  const classes = useStyles();
  return (
    <div className="fixHeader">
      <AppBar position="static" color="secondary">
        <Toolbar>
        <Box sx = {{width:30}}></Box>
          <Typography variant="h6" className={classes.title}>
          <a href="/"> <img src= {logo} alt="picture" width = "350"/></a>
          </Typography>
          <Button color="inherit" component={Link} to = "/fromTweet">Tweetから生成</Button>
          <Button color="inherit" component={Link} to = "/fromCopus">コーパスから生成</Button>
          <Button color="inherit" component={Link} to = "/rules">利用規約</Button>
        </Toolbar>
      </AppBar>
    </div>
  );
}

