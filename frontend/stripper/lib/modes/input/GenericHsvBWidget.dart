import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:sleek_circular_slider/sleek_circular_slider.dart';

class GenericHsvBWidget extends StatefulWidget {
  final String label;
  final double startValue;
  final ValueChanged<double> onChangeEnd;

  GenericHsvBWidget({required this.label, required this.onChangeEnd, required this.startValue});
  @override
  State<StatefulWidget> createState() => _GenericHsvBState();
}

class _GenericHsvBState extends State<GenericHsvBWidget> {
  double _sliderValue = 0;

  @override
  void initState() {
    _sliderValue = widget.startValue;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Wrap(children: [
      Text(widget.label),
      Slider(
        onChangeEnd: (double value) => widget.onChangeEnd(value),
        onChanged: (double value) => setState(() {
          _sliderValue = value;
        }),
        value: _sliderValue,
      )
    ]);
  }
}
