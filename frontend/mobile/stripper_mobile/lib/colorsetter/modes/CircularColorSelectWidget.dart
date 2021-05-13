import 'package:flutter/material.dart';
import 'package:sleek_circular_slider/sleek_circular_slider.dart';

class CircularColorSelectWidget extends StatelessWidget {
  final Function(double) onColorChanged;

  CircularColorSelectWidget({Key key, @required this.onColorChanged})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width.clamp(300, 500);
    return ConstrainedBox(
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
          onChangeStart: (double startValue) {},
          onChangeEnd: (double endValue) {
            onColorChanged(endValue);
          },
        ));
  }
}
