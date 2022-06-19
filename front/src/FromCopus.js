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
import { Container, Grid } from '@material-ui/core';

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

export default function FromCopus(){
    return(
      <div>
      <Box sx = {{height:100}}></Box>
      <Box sx={{ bgcolor: '#ffffff', width: 900,  borderRadius: '16px'}}>
      <Container maxWidth="sm" >
      <Box sx = {{height:50}}></Box>
    <h2>コーパスから生成</h2>
    <Box sx = {{height:100}}></Box>
    </Container>
    </Box>
    <Box sx = {{height:100}}></Box>
    </div>
    );
  }

  function getCorpus(){
    return(
      <div>
        
      </div>
    );
  }