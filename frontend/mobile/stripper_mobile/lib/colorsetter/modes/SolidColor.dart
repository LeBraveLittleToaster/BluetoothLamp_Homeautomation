import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:stripper_mobile/colorsetter/modes/CircularColorSelectWidget.dart';
import 'package:stripper_mobile/net/requester.dart';
import 'package:stripper_mobile/types/device.dart';
import 'package:stripper_mobile/types/modes.dart';

class SolidColorWidget extends StatefulWidget {
  final Device device;
  SolidColorWidget({Key key, @required this.device}) : super(key: key);

  @override
  State<StatefulWidget> createState() => new _SolidColorState();
}

class _SolidColorState extends State<SolidColorWidget> {
  double colorAngle = 0;
  double brightness = 150;

  _onChange(double nColorAngle, double nBrightnes) {
    setState(() {
      colorAngle = nColorAngle;
      brightness = nBrightnes;
    });
    print("SENDING:  colorAngle=" +
        colorAngle.toString() +
        " | Brightness=" +
        brightness.toString());
    Requester.setDeviceMode(widget.device.uuid,
        ModeSolidColor(
          hue: colorAngle.round().clamp(0, 255),
          value: 255,
          saturation: 255,
          brightness: brightness.round().clamp(0, 255)));
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
                    _onChange(angle, brightness);
                  },
                ),
                Padding(
                  padding: EdgeInsets.fromLTRB(0, 25, 0, 15),
                  child: Text(
                    "Brightness",
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
                    value: brightness,
                    min: 0,
                    max: 255,
                    onChanged: (value) {
                      setState(() {
                        brightness = value;
                      });
                    },
                    onChangeEnd: (value) {
                      _onChange(colorAngle, value);
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
