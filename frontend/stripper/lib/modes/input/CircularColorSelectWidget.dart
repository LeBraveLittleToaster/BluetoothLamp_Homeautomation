import 'package:flutter/material.dart';
import 'package:sleek_circular_slider/sleek_circular_slider.dart';
import 'package:stripper/types/ParamValue.dart';

class CircularColorSelectWidget extends StatefulWidget {
  final Function(double, double) onColorChanged;
  final ParamValue? initParam;

  CircularColorSelectWidget(
      {required this.onColorChanged, required this.initParam});

  @override
  State<StatefulWidget> createState() => _CircularColorSelectState();
}

class _CircularColorSelectState extends State<CircularColorSelectWidget> {
  double brightness = 0;
  double angle = 0;

  @override
  void initState() {
    try {
      brightness = widget.initParam!.value[3];
      angle = widget.initParam!.value[0];
    } catch (error) {
      print("Wrong or no initValue");
      print(error);
    }
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width.clamp(300, 500);
    return ConstrainedBox(
        constraints: BoxConstraints(minWidth: 300, maxWidth: 800),
        child: SleekCircularSlider(
          appearance: CircularSliderAppearance(
              animationEnabled: false,
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
                  dotColor: Colors.white,
                  hideShadow: true,
                  dynamicGradient: false,
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
          initialValue: angle,
          innerWidget: (angle) => Center(
            child: Wrap(
              direction: Axis.vertical,
              crossAxisAlignment: WrapCrossAlignment.center,
              children: [
                IconButton(
                    iconSize: 60,
                    icon: Icon(Icons.arrow_drop_up_sharp),
                    onPressed: () {
                      setState(() {
                        brightness = (brightness + 0.1).clamp(0, 1);
                      });
                      widget.onColorChanged(angle, brightness);
                    }),
                Container(
                  width: width * 0.3,
                  height: 20,
                  decoration: BoxDecoration(
                      color: Color.lerp(Colors.black, Colors.white, brightness),
                      borderRadius: BorderRadius.circular(10)),
                ),
                IconButton(
                    iconSize: 60,
                    icon: Icon(Icons.arrow_drop_down),
                    onPressed: () {
                      setState(() {
                        brightness = (brightness - 0.1).clamp(0, 1);
                      });
                      widget.onColorChanged(angle, brightness);
                    })
              ],
            ),
          ),
          onChangeStart: (double startValue) {},
          onChangeEnd: (double endValue) {
            setState(() {
              angle = endValue;
            });
            widget.onColorChanged(endValue, brightness);
          },
        ));
  }
}
