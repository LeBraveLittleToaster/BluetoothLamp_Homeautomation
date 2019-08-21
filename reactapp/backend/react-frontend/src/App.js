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

  onUpdateClicked() {
    console.log("LOL")
  }

  render() {
    return (
      <div className="windowFrame">
        <h1 className="headline">LED CONTROL CENTER</h1>
        <a className="float" onClick={this.onUpdateClicked.bind(this)}>
          <i className="fa fa-plus my-float">Update</i>
        </a>
        <Grid container spacing={3}>
          <Grid item className="leftContainer" xs={6}>
            <div>
            <Grid container spacing={3}>
              <Grid item xs={6}>A</Grid>
              <Grid item xs={6}>B</Grid>
              <Grid item xs={6}>C</Grid>
              <Grid item xs={6}>D</Grid>
            </Grid>
            </div>
          </Grid>
          <Grid item className="rightContainer" xs={6}>
            <Grid container spacing={3}>
              {this.state.strips.map((object, i) => <Grid item xs={8}> <Paper className='paper'><StripView strip={object} key={i} /> </Paper> </Grid>)}
            </Grid>
          </Grid>
        </Grid>
        <div className="lowerFrame">
          <h2 className="subInfo">Create by Pascal Schiessle</h2>
          <h2 className="subInfo">Powered by React.js</h2>
        </div>
      </div>
    );
  }
}

export default App;
