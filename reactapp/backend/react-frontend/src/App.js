import React, { Component } from 'react';
import './App.css';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import axios from 'axios'
import StripView from './StripView';

class App extends Component {

  constructor(props) {
    super(props)
    this.state = { "strips": [{ "id": 0, "mode": { "mode_color_b": 255, "mode_color_g": 0, "mode_color_r": 0, "mode_id": 1 }, "name": "Right Shelf" }, { "id": 1, "mode": { "mode_color_b": 255, "mode_color_g": 0, "mode_color_r": 0, "mode_id": 2 }, "name": "Left Shelf" }] }
  }

  componentDidMount() {
    /*
    axios.get('http://localhost:5000/strips').then(res => {
      const strips = res.data;
      this.setState(strips)
    })
    */
    //this.setState = 
  }

  render() {
    return (
      <div className="windowFrame">
        <h1 className="headline">LED CONTROL CENTER</h1>

        
        <div className="splitLeftContainer">

        </div>
        <div className="splitRightContainer">
          <Grid container spacing={3}>
            {this.state.strips.map((object, i) => <Grid item xs={12}> <Paper className='paper'><StripView strip={object} key={i} /> </Paper> </Grid>)}
          </Grid>
        </div>
      </div>
      /*
      <div className="windowFrame">
        <div className="grid-container">
          <Grid container spacing={3}>
            {this.state.strips.map((object, i) => <Grid item xs={12}> <Paper className='paper'><StripView strip={object} key={i} /> </Paper> </Grid>)}
          </Grid>
        </div>
        <h1 className="headline">LED CONTROL CENTER</h1>
        <h2 className="header-second">Created with React.js by Pascal Schiessle</h2>
      </div>
      */
    );
  }
}

export default App;
