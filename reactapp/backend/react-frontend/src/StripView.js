import React, { Component } from 'react';
import './App.css';


class StripView extends Component {

  constructor(props){
    super(props)
    this.state = props.strip
  }

  componentDidMount(){
   this.setState = {"strips":[{"id":0,"mode":{"mode_color_b":255,"mode_color_g":0,"mode_color_r":0,"mode_id":1},"name":"Right Shelf"},{"id":1,"mode":{"mode_color_b":255,"mode_color_g":0,"mode_color_r":0,"mode_id":2,"mode_speed":0.5},"name":"Left Shelf"}]}
  }

  render() {
      var id = this.state.id
    return (
        <div >
            <h1>MyId={id}</h1>
        </div>
    );
  }
}

export default StripView;
