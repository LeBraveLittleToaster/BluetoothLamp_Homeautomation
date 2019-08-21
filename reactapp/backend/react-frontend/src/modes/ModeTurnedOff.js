import React, { Component } from 'react';
import './ModeStyle.css';

class ModeTurnOff extends Component{

    constructor(props){
        super(props)

    }

    componentDidMount(){
        this.props.callback({"mode_id" : 0})
    }

    componentDidUpdate(){
        this.props.callback({"mode_id" : 0})
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