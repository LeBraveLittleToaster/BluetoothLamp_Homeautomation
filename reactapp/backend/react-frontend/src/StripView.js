import React, { Component } from 'react';
import Select from 'react-select';
import './StripView.css';
import './App.css';
import ModeTurnedOff from './modes/ModeTurnedOff'
import ModeSolidColor from './modes/ModeSolidColor'
import ModeSingleColorWave from './modes/ModeSingleColorWave'
import ModeMultiColorWave from './modes/ModeMultiColorWave'
import ModeSingleColorFlicker from './modes/ModeSingleColorFlicker'
import ModeMultiColorFlicker from './modes/ModeMultiColorFlicker'
import ModeSingleColorPulse from './modes/ModeSingleColorPulse'

const options = [
    { value: 0, label: "Off" },
    { value: 1, label: "Solid Color" },
    { value: 2, label: "Single Colorramp" },
    { value: 3, label: "Rainbow Colorramp" },
    { value: 4, label: "Single Flicker" },
    { value: 5, label: "Rainbow Flicker" },
    { value: 6, label: "Single Colorpulse" },
]



class StripView extends Component {

    constructor(props) {
        super(props)
        this.state = {
            selectedOption: options[this.props.strip.mode.mode_id],
            strip: this.props.strip
        }
    }

    componentDidUpdate() {
        this.props.callback(this.props.id, this.state.strip);
    }

    getModeData(mode) {
        this.state.strip.mode = mode;
        this.props.callback(this.props.id, this.state.strip)
    }

    getModeOptionsDiv() {
        switch (this.state.selectedOption.value) {
            case 0:
                return (<ModeTurnedOff strip={this.state.strip} callback={this.getModeData.bind(this)} />);
            case 1:
                return (<ModeSolidColor strip={this.state.strip} callback={this.getModeData.bind(this)} />);
            case 2:
                return (<ModeSingleColorWave strip={this.state.strip} callback={this.getModeData.bind(this)} />);
            case 3:
                return (<ModeMultiColorWave strip={this.state.strip} callback={this.getModeData.bind(this)} />);
            case 4:
                return (<ModeSingleColorFlicker strip={this.state.strip}callback={this.getModeData.bind(this)} />);
            case 5:
                return (<ModeMultiColorFlicker strip={this.state.strip}callback={this.getModeData.bind(this)} />);
            case 6:
                return (<ModeSingleColorPulse strip={this.state.strip}callback={this.getModeData.bind(this)} />);
            default:
                return (<div><h1>Choose mode or Error</h1></div>)
        }
    }

    handleChange = selectedOption => {
        this.setState({ selectedOption: selectedOption, strip: this.state.strip })
        console.log('Option selected:', selectedOption)
    }

    componentDidUpdate() {
        console.log(JSON.stringify(this.state))
        this.props.callback(this.props.id, this.state.strip)
    }

    render() {
        const { selectedOption } = this.state.selectedOption
        return (
            <div className="bgCard">
                <h1 className="headers">{this.state.strip.name}</h1>
                <Select 
                    maxMenuHeight={300}
                    value={selectedOption}
                    onChange={this.handleChange}
                    options={options}
                    placeholder={this.state.selectedOption.label}
                    readonly
                />
                {this.getModeOptionsDiv()}
            </div>
        )
    }
}

export default StripView;
