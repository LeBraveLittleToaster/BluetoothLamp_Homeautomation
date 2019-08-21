import React, { Component } from 'react';
import './ModeStyle.css';
import Slider from 'react-input-slider';
import {ifPresent} from './ModeUtils';
var mathClamp = require('math-clamp');


class ModeMultiColorWave extends Component{
    constructor(props) {
        super(props)
        this.state = {
            speed: mathClamp(Math.floor(ifPresent(props.strip.mode.speed, 0) * 0.4), 0 , 255),
            shift_speed: mathClamp(Math.floor(ifPresent(props.strip.mode.shift_speed, 0) * 0.4), 0 , 255),
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
            "mode_id" : 3,
            "mode_color_h" : 0,
            "mode_color_s": 0,
            "mode_color_v": 0,
            "speed": mathClamp(Math.floor(this.state.speed * 2.5), 0 , 255),
            "shift_speed": mathClamp(Math.floor(this.state.shift_speed * 2.5), 0 , 255)
        }
    }

    render(){
        return (
            <div>
                <h2 className="speedHeader">MOVEMENT SPEED</h2>
                <p className="valueNumberDisplay">{this.state.speed}</p>
                <Slider 
                    styles={{thumb: {width: 25, height: 25}, track: {width: "90%"}}}
                    axis="x"
                    x={this.state.speed}
                    onChange={(value) => {this.setState({speed: value.x})}}
                />
                <h2 className="speedHeader">COLOR SHIFT SPEED</h2>
                <p className="valueNumberDisplay">{this.state.shift_speed}</p>
                <Slider 
                    styles={{thumb: {width: 25, height: 25}, track: {width: "90%"}}}
                    axis="x"
                    x={this.state.shift_speed}
                    onChange={(value) => {this.setState({shift_speed: value.x})}}
                />
            </div>
        )
    }
}

export default ModeMultiColorWave;
