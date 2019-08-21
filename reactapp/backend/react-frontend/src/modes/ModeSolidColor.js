import React, { Component } from 'react';
import './ModeStyle.css';
import Slider from 'react-input-slider';
import HSVtoRGB from "./ModeUtils";

class ModeSolidColor extends Component{
    constructor(props) {
        super(props)
        this.state = {hue:0}
    }

    componentDidUpdate(){
        this.props.callback({"mode" : "mode1"})
    }

    render(){
        let cFieldColor = HSVtoRGB((this.state.hue / 100.0), 1 , 1);
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
            </div>
        )
    }
}



export default ModeSolidColor;