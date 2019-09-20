import React, { Component } from 'react';
import './App.css';
import Grid from '@material-ui/core/Grid';
import axios from 'axios'
import StripView from './StripView';
import update from 'immutability-helper';

class App extends Component {

  constructor(props) {
    super(props)
    this.state = { "strips": [{ "id": 0, "mode": { "mode_color_h": 50, "mode_color_s": 0, "mode_color_v": 0, "mode_id": 1 }, "name": "Right Shelf" }, { "id": 1, "mode": { "mode_color_h": 255, "mode_color_s": 0, "mode_color_v": 0, "speed": 250, "mode_id": 2 }, "name": "Left Shelf" }] }
    //this.state = null;
  }

  async componentDidMount() {
    await axios.get('http://localhost:5000/strips/').then(res => {
      const strips = res.data;
      console.log("Collected data: " + strips);
      this.setState(strips)
      console.log("State data: " + JSON.stringify(this.state));
      this.forceUpdate();
    }).catch(console.log)
  }

  async onUpdateClicked() {
    console.log(JSON.stringify(this.state.strips))
    axios.post('http://localhost:5000/strips/set', JSON.stringify(this.state), { headers: { 'Content-Type': 'application/json' } }).then(res => {
      const success = res.data.success;
      console.log("Post is success: " + success)
    })
  }
  async onReconnect() {
    console.log("Reconnecting")
    axios.get('http://localhost:5000/strips/reconnect', JSON.stringify(this.state), { headers: { 'Content-Type': 'application/json' } });
  }

  updateData(index, strip) {
    this.state.strips[index].mode = strip.mode;
    console.log("On update")
    console.log(strip.mode)
  }

  render() {
    if (this.state === null || this.state === undefined){
      console.log("No state");
      return (<div className="windowFrame"><h1 className="headline">Waiting for data...</h1></div>);
    } else if(this.state.strips === null || this.state.strips === undefined) {
      console.log("Strips null");
      return (<div className="windowFrame"><h1 className="headline">Waiting for data...</h1></div>);
    } else {
      return (
        <div className="windowFrame">
          <br/><br/><br/><br/><br/>
          <a className="float" onClick={this.onUpdateClicked.bind(this)}>
            <i className="fa fa-plus my-float">Update</i>
          </a>
          <div className="gridContainer">
            <Grid container spacing={3}>
              {this.state.strips.map(e => {
                return (
                  <Grid key={e.id} item xs={6}>
                    <div key={e.id} className="paper">
                      <StripView id={e.id} key={e.id} strip={e} callback={this.updateData.bind(this)} />
                    </div>
                  </Grid>
                )
              }
              )}
            </Grid>
          </div>
          <div className="lowerFrame">
            <h2 className="subInfo">Create by Pascal Schiessle</h2>
            <h2 className="subInfo unselectable">Powered by React.js</h2>

            <div onClick={this.onReconnect.bind(this)} className="reconnect_btn unselectable">
              <a>
                <i>Reconnect</i>
              </a>
            </div>
          </div>
        </div>
      );
    }
  }
}

export default App;
