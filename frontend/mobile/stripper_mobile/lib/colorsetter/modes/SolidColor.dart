import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:sleek_circular_slider/sleek_circular_slider.dart';
import 'package:stripper_mobile/types/device.dart';

class SolidColorWidget extends StatefulWidget {
  final Device device;
  SolidColorWidget({Key key, @required this.device}) : super(key: key);

  @override
  State<StatefulWidget> createState() => new _SolidColorState();
}

class _SolidColorState extends State<SolidColorWidget> {
  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width.clamp(300, 500);
    print("WIDTH SLIDER: " + width.toString());

    return SingleChildScrollView(
        scrollDirection: Axis.vertical,
        child: Padding(
          padding: EdgeInsets.fromLTRB(0, 50, 0, 0),
          child: Row(
            children: [
              Expanded(
                child: Container(),
              ),
              ConstrainedBox(
                constraints: BoxConstraints(minWidth: 300, maxWidth: 800),
                child: SleekCircularSlider(
                  appearance: CircularSliderAppearance(
                      startAngle: 0,
                      angleRange: 360,
                      customWidths: CustomSliderWidths(
                          progressBarWidth: width / 8,
                          handlerSize: width / 16,
                          shadowWidth: 0,
                          trackWidth: width / 8),
                      customColors: CustomSliderColors(
                          progressBarColor: Color.fromRGBO(0, 0, 0, 0),
                          shadowColor: Color.fromRGBO(0, 0, 0, 0),
                          trackGradientStartAngle: 0,
                          trackGradientEndAngle: 360,
                          trackColors: [
                            Colors.red,
                            Colors.orange,
                            Colors.yellow,
                            Colors.green,
                            Colors.cyan,
                            Colors.blue,
                            Colors.purple,
                            Colors.pink,
                            Colors.red
                          ]),
                      size: width * 0.8),
                  min: 0,
                  max: 255,
                  initialValue: 0,
                  innerWidget: (angle) => Container(),
                  onChangeStart: (double startValue) {
                    print(MediaQuery.of(context).size.toString());
                  },
                  onChangeEnd: (double endValue) {
                    // ucallback providing an ending value (when a pan gesture ends)
                  },
                ),
              ),
              Expanded(child: Container())
            ],
          ),
        ));
  }
}
