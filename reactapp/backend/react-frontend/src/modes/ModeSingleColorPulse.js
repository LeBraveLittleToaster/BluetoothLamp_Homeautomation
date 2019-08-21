import React, { Component } from 'react';
import './ModeStyle.css';
import Slider from 'react-input-slider';
import {HSVtoRGB, ifPresent} from "./ModeUtils";
var mathClamp = require('math-clamp');


class ModeSingleColorPulse extends Component{
    constructor(props) {
        super(props)
        this.state = {
            mode_color_h: mathClamp(Math.floor(ifPresent(props.strip.mode.mode_color_h, 0)* 0.4), 0, 100),
            pulse_speed: mathClamp(Math.floor(ifPresent(props.strip.mode.pulse_speed, 0)* 0.4), 0, 100),
        }
    }

    componentDidMount(){
        this.props.callback(this.getUpdateCall())
    }

    componentDidUpdate(){
        this.props.callback(this.getUpdateCall())
    }

    getUpdateCall(){
        return {
            "mode_id" : 6,
            "mode_color_h" : mathClamp(Math.floor(this.state.mode_color_h * 2.5), 0 , 255),
            "mode_color_s": 255,
            "mode_color_v": 255,
            "pulse_speed": mathClamp(Math.floor(this.state.pulse_speed * 2.5), 0 , 255)
        }
    }

    render(){
        let cFieldColor = HSVtoRGB((this.state.mode_color_h / 100.0), 1 , 1);
        let colorStr = "rgb(" + cFieldColor.r + "," + cFieldColor.g + ","+ cFieldColor.b + ")";
        return (
            
            <div>
                <h2>COLOR</h2>
                <div className="colorField" style={{backgroundColor: colorStr}}></div>
                <Slider 
                    styles={{thumb: {width: 25, height: 25}, track: {width: "90%"}}}
                    axis="x"
                    x={this.state.mode_color_h}
                    onChange={(value) => {this.setState({mode_color_h: value.x})}}
                />

                <h2 className="speedHeader">PULSE SPEED</h2>
                <p className="valueNumberDisplay">{this.state.pulse_speed}</p>
                <Slider 
                    styles={{thumb: {width: 25, height: 25}, track: {width: "90%"}}}
                    axis="x"
                    x={this.state.pulse_speed}
                    onChange={(value) => {this.setState({pulse_speed: value.x})}}
                />
            </div>
        )
    }
}

export default ModeSingleColorPulse;
