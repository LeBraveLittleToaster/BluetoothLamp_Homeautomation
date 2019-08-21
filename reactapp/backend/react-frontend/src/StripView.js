import React, { Component } from 'react';
import Select from 'react-select';
import './StripView.css';
import './App.css';
import ModeTurnedOff from './modes/ModeTurnedOff'
import ModeSolidColor from './modes/ModeSolidColor'
import ModeSingleColorWave from './modes/ModeSingleColorWave'

const options = [
    {value: 0, label: "Off"},
    {value: 1, label: "Mode1"},
    {value: 2, label: "Mode2"}
]



class StripView extends Component {

    constructor(props) {
        super(props)
        this.state = {
            selectedOption: this.props.strip.mode.mode_id,
            strip: this.props.strip
        }
    }

    componentDidUpdate(){
        this.props.callback(this.props.key, this.state.strip);
    }

    getModeData(mode){
        this.state.strip.mode = mode
    }

    getModeOptionsDiv(){
        switch(this.state.selectedOption.value){
            case 0:
                return (<ModeTurnedOff callback={this.getModeData.bind(this)}/>);
            case 1:
                return (<ModeSolidColor callback={this.getModeData.bind(this)}/>);
            case 2:
                return (<ModeSingleColorWave callback={this.getModeData.bind(this)}/>);
                default:
                    return (<div><h1>Choose mode or Error</h1></div>)
        }
    }

    handleChange = selectedOption => {
        this.setState({selectedOption: selectedOption, strip: this.state.strip})
        console.log('Option selected:' , selectedOption)
    }

    componentDidUpdate() {
        this.props.callback(this.props.id, )
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
