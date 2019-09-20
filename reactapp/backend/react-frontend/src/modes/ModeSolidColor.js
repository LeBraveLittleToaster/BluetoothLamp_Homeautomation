import React, { Component } from 'react';
import './ModeStyle.css';
import Slider from 'react-input-slider';
import {HSVtoRGB, ifPresent} from "./ModeUtils";
var mathClamp = require('math-clamp');


class ModeSolidColor extends Component{
    constructor(props) {
        super(props)
        this.state = {
            hue: mathClamp(Math.floor(ifPresent(props.strip.mode.mode_color_h, 0)* 0.4), 0, 100),
            saturation: mathClamp(Math.floor(ifPresent(props.strip.mode.mode_color_s, 0)* 0.4), 0, 100),
            value: mathClamp(Math.floor(ifPresent(props.strip.mode.mode_color_v, 0)* 0.4), 0, 100),
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
            "mode_id" : 1,
            "mode_color_h" : mathClamp(Math.floor(this.state.hue * 2.5) , 0 , 255),
            "mode_color_s": mathClamp(Math.floor(this.state.saturation * 2.5) , 0 , 255),
            "mode_color_v": mathClamp(Math.floor(this.state.value * 2.5) , 0 , 255),
        }
    }

    render(){
        let cFieldColor = HSVtoRGB((this.state.hue / 100.0), (this.state.saturation / 100.0) , (this.state.value / 100.0));
        let colorStr = "rgb(" + cFieldColor.r + "," + cFieldColor.g + ","+ cFieldColor.b + ")";
        return (
            
            <div>
                <h2>COLOR</h2>
                <div className="colorField" style={{backgroundColor: colorStr}}></div>
                <Slider 
                    styles={{thumb: {width: 25, height: 25}, track: {width: "90%"}}}
                    axis="x"
                    x={this.state.hue}
                    onChange={(value) => this.setState({hue: value.x})}
                />
                <h2>SATURATION</h2>
                <Slider 
                    styles={{thumb: {width: 25, height: 25}, track: {width: "90%"}}}
                    axis="x"
                    x={this.state.saturation}
                    onChange={(value) => this.setState({saturation: value.x})}
                />
                <h2>VALUE</h2>
                <Slider 
                    styles={{thumb: {width: 25, height: 25}, track: {width: "90%"}}}
                    axis="x"
                    x={this.state.value}
                    onChange={(value) => this.setState({value: value.x})}
                />
            </div>
        )
    }
}



export default ModeSolidColor;