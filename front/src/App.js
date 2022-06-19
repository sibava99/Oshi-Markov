import React from 'react';
import './App.css';
import Header from './Header.js'
import Home from './Home.js'
import FromTweet from './FromTweet.js'
import FromCopus from './FromCopus.js'
import Rules from './Rules.js'
import Box from '@mui/material/Box';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Container from '@mui/material/Container';

class App extends React.Component {
  constructor(props,context){
    super(props,context)
    
  }
  render(){
    return (
      <BrowserRouter>
      <Box sx={{ bgcolor: '#f0e9f6'}}>
        <div>
        <Header/>
        <Container>
            <Routes>
            <Route exaxt path="/" element = {<Home />} />
            <Route path="fromTweet" element = {<FromTweet />} />
            <Route path="fromCopus" element = {<FromCopus />} />
            <Route path="rules" element = {<Rules />} />
            <Route element = {<NotFound />} />
            </Routes>
            </Container>
        </div>
        </Box>
        </BrowserRouter>
    );
  }
}

function NotFound(){
  return <h2>NOT FOUND PAGE</h2>;
}

export default App;