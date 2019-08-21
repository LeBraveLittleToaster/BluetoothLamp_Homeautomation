import React, { Component } from 'react';
import Select from 'react-select';
import './StripView.css';
import './App.css';

const options = [
    {value: 0, label: "Off"},
    {value: 1, label: "Mode1"},
    {value: 2, label: "Mode2"}
]



class StripView extends Component {

    constructor(props) {
        super(props)
        this.state = {
            selectedOption: props.strip.mode.mode_id,
            strip: props.strip
        }
    }

    getModeOptionsDiv(){
        switch(this.state.selectedOption.value){
            case 0:
                return (<div/>);
            case 1:
                return (<div/>);
            case 2:
                return (<div/>);
                default:
                    return (<div><h1>Choose mode or Error</h1></div>)
        }
    }

    handleChange = selectedOption => {
        this.setState({selectedOption: selectedOption, strip: this.state.strip})
        console.log('Option selected:' , selectedOption)
    }

    render() {
        const { selectedOption } = this.state.selectedOption
        return (
            <div className="bgCard">
                <h1 className="headers">{this.state.strip.name}</h1>
                <Select className="select-border"
                    value={selectedOption}
                    onChange={this.handleChange}
                    options={options}
                    placeholder={"Choose Mode"}
                />
            {this.getModeOptionsDiv()}
            </div>
        )
    }
}

export default StripView;
