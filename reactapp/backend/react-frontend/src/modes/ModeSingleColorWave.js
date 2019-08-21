import React, { Component } from 'react';
import './ModeStyle.css';
import Slider from 'react-input-slider';
import HSVtoRGB from "./ModeUtils";

class ModeSingleColorWave extends Component{
    constructor(props) {
        super(props)
        this.state = {x:0, speed: 1}
    }

    componentDidUpdate(r1 , r2){
        this.props.callback({"mode" : "mode2"})
    }

    render(){
        let cFieldColor = HSVtoRGB((this.state.x / 100.0), 1 , 1);
        let colorStr = "rgb(" + cFieldColor.r + "," + cFieldColor.g + ","+ cFieldColor.b + ")";
        return (
            
            <div>
                <h2>COLOR</h2>
                <div className="colorField" style={{backgroundColor: colorStr}}></div>
                <Slider 
                    styles={{thumb: {width: 25, height: 25}, track: {width: "90%"}}}
                    axis="x"
                    x={this.state.x}
                    onChange={(value) => {this.setState({x: value.x})}}
                />
                <h2 className="speedHeader">SPEED</h2>
                <p className="valueNumberDisplay">{this.state.speed}</p>
                <Slider 
                    styles={{thumb: {width: 25, height: 25}, track: {width: "90%"}}}
                    axis="x"
                    x={this.state.speed}
                    onChange={(value) => {this.setState({speed: value.x})}}
                />
            </div>
        )
    }
}

export default ModeSingleColorWave;
