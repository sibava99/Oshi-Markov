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

import {
  useParams,
  useHistory,
  useLocation,
} from 'react-router-dom';

export default function App(props){
  return(
    <BrowserRouter>
      <Box sx={{ bgcolor: '#f0e9f6'}}>
        <div>
          <Header/>
          <Container>
            <Routes>
              <Route path="fromTweet" element = {<FromTweet />} />
              <Route path="fromCopus" element = {<FromCopus />} />
              <Route path="rules" element = {<Rules />} />
              <Route path="/:model_id" element = {<Home />} />
              <Route element = {<NotFound />} />
            </Routes>
          </Container>
        </div>
      </Box>
    </BrowserRouter>
  )
}

function NotFound(){
  return <h2>NOT FOUND PAGE</h2>;
}