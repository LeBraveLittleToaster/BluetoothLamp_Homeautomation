import React, { Component } from 'react';
import './App.css';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import axios from 'axios'
import StripView from './StripView';

class App extends Component {

  constructor(props){
    super(props)
    this.state = {"strips":[{"id":0,"mode":{"mode_color_b":255,"mode_color_g":0,"mode_color_r":0,"mode_id":1},"name":"Right Shelf"}]}
  }

  componentDidMount(){

    axios.get('http://localhost:5000/strips').then(res => {
      const strips = res.data;
      this.setState(strips)
    })
   //this.setState = 
  }

  render() {
    return (
      <div>
        <Grid container spacing={3}>
          {this.state.strips.map((object, i) => <Grid item xs = {6}> <Paper className='paper'><StripView strip={object} key={i}/> </Paper> </Grid>)}
        </Grid>    
      </div>
    );
  }
}

export default App;
