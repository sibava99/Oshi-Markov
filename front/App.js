import React from 'react';
import './App.css';
import Header from './Header.js'
import Home from './Home.js'
import FromTweet from './FromTweet.js'
import { BrowserRouter, Route, Routes } from 'react-router-dom';

class App extends React.Component {
  constructor(props,context){
    super(props,context)
    
  }
  render(){
    return (
      <BrowserRouter>
        <div>
            <Header/>
            <Routes>
            <Route exaxt path="/" element = {<Home />} />
            <Route path="fromTweet" element = {<FromTweet />} />
            <Route path="fromCopus" element = {<FromCopus />} />
            <Route path="rules" element = {<Rules />} />
            <Route element = {<NotFound />} />
            </Routes>
        </div>
        </BrowserRouter>
    );
  }
}

function NotFound(){
  return <h2>NOT FOUND PAGE</h2>;
}

export default App;