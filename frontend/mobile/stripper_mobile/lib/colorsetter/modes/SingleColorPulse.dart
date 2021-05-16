import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:stripper_mobile/colorsetter/modes/CircularColorSelectWidget.dart';
import 'package:stripper_mobile/net/requester.dart';
import 'package:stripper_mobile/types/device.dart';
import 'package:stripper_mobile/types/modes.dart';

class SingleColorPulseWidget extends StatefulWidget {
  final Device device;
  SingleColorPulseWidget({Key key, @required this.device}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _SingleColorPulseState();
}

class _SingleColorPulseState extends State<SingleColorPulseWidget> {
  double colorAngle = 0;
  RangeValues brightness = RangeValues(0, 255);
  double speed = 0;

  @override
  void initState() {
    if (widget.device.state.mode != null &&
        widget.device.state.mode.mode_id == 2) {
      ModeSingleColorPulse pulse = widget.device.state.mode;
      brightness = RangeValues(
          pulse.brightness_start.toDouble(), pulse.brightness_end.toDouble());
      colorAngle = pulse.hue.toDouble();
      speed = pulse.speed.toDouble();
    }
    super.initState();
  }

  _onChange(double nColorAngle, RangeValues nBrightnes, double nSpeed) {
    setState(() {
      colorAngle = nColorAngle;
      brightness = nBrightnes;
      speed = nSpeed;
    });
    print("SENDING:  colorAngle=" +
        colorAngle.toString() +
        " | BrightnessRange=" +
        brightness.toString() +
        " | speed=" +
        speed.toString());
    Requester.setDeviceMode(
        widget.device.uuid,
        ModeSingleColorPulse(
            hue: colorAngle.round().clamp(0, 255),
            value: 255,
            saturation: 255,
            brightness: brightness.start.round().clamp(0, 255),
            brightness_start: brightness.start.round().clamp(0, 255),
            brightness_end: brightness.end.round().clamp(0, 255),
            speed: speed.round().clamp(0, 255)));
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: SingleChildScrollView(
        scrollDirection: Axis.vertical,
        child: Padding(
          padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
          child: Center(
              child: ConstrainedBox(
            constraints: BoxConstraints(minWidth: 300, maxWidth: 500),
            child: Column(
              children: [
                Padding(
                  padding: EdgeInsets.fromLTRB(0, 25, 0, 15),
                  child: Text(
                    "Color",
                    style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                  ),
                ),
                CircularColorSelectWidget(
                  onColorChanged: (angle) {
                    _onChange(angle, brightness, speed);
                  },
                ),
                Padding(
                  padding: EdgeInsets.fromLTRB(0, 25, 0, 15),
                  child: Text(
                    "Brightness Range",
                    style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                  ),
                ),
                SliderTheme(
                  data: SliderTheme.of(context).copyWith(
                    trackHeight: 70,
                    thumbShape: RoundSliderThumbShape(
                        enabledThumbRadius: 36, elevation: 0),
                  ),
                  child: RangeSlider(
                    values: brightness,
                    min: 0,
                    max: 255,
                    onChanged: (value) {
                      setState(() => brightness = value);
                    },
                    onChangeEnd: (value) {
                      _onChange(colorAngle, value, speed);
                    },
                  ),
                ),
                Padding(
                  padding: EdgeInsets.fromLTRB(0, 10, 0, 15),
                  child: Text(
                    "Speed",
                    style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                  ),
                ),
                SliderTheme(
                  data: SliderTheme.of(context).copyWith(
                    trackHeight: 70,
                    thumbShape: RoundSliderThumbShape(
                        enabledThumbRadius: 36, elevation: 0),
                  ),
                  child: Slider(
                    value: speed,
                    min: 0,
                    max: 255,
                    onChanged: (value) {
                      setState(() {
                        speed = value;
                      });
                    },
                    onChangeEnd: (value) {
                      _onChange(colorAngle, brightness, value);
                    },
                  ),
                )
              ],
            ),
          )),
        ),
      ),
    );
  }
}
