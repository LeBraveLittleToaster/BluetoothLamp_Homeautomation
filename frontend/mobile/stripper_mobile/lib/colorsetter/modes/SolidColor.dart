import 'package:flutter/material.dart';
import 'package:sleek_circular_slider/sleek_circular_slider.dart';

class SolidColorWidget extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => new _SolidColorState();
}

class _SolidColorState extends State<SolidColorWidget> {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: SleekCircularSlider(
          appearance: CircularSliderAppearance(
              customWidths: CustomSliderWidths(
                  progressBarWidth: 40,
                  handlerSize: 30,
                  shadowWidth: 0,
                  trackWidth: 20),
              customColors: CustomSliderColors(progressBarColors: [
                Colors.grey,
                Colors.grey,
              ], trackColors: [
                Colors.grey,
                Colors.grey,
              ]),
              size: MediaQuery.of(context).size.width * 0.8),
          min: 0,
          max: 255,
          initialValue: 0,
          onChangeStart: (double startValue) {
            // callback providing a starting value (when a pan gesture starts)
          },
          onChangeEnd: (double endValue) {
            // ucallback providing an ending value (when a pan gesture ends)
          },
        ),
    );
  }
}
