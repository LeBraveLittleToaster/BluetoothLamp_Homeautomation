import React from 'react';
import {HuePicker} from 'react-color';
import './StripViewTemplates.css'
class StripViewTemplates {

    turnOffDiv = (
        <div>
            <h1>Strip is turned off</h1>
        </div>
    )
    mode1Div = (
        <div className="picker">
            <h2>Color</h2>
            <HuePicker/>
        </div>)
    mode2Div = (
        <div className="picker">
            <h2>Color</h2>
            <HuePicker/>
            <br/>
            <h2>Speed</h2>
        </div>
    )
}
module.exports=StripViewTemplates