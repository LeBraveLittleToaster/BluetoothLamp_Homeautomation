import React, { Component } from 'react';
import './ModeStyle.css';

class ModeTurnOff extends Component{

    constructor(props){
        super(props)

    }

    componentDidUpdate(){
        this.props.callback({"mode" : "mode0"})
    }    

    render(){
        return (
            <div>
                <h2>Strip is turned off...</h2>
            </div>
        )
    }
}

export default ModeTurnOff;