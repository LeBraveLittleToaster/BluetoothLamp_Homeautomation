import 'package:flutter/material.dart';
import 'package:stripper/modes/ModeDefinition.dart';
import 'package:stripper/types/ParamResult.dart';

class HsvBWidget extends StatefulWidget {
  final String label;
  final ParamResult startValue;
  final ValueChanged<ParamResult> onChangeEnd;

  HsvBWidget(
      {required this.label,
      required this.onChangeEnd,
      required this.startValue});
  @override
  State<StatefulWidget> createState() => _HsvBState();
}

class _HsvBState extends State<HsvBWidget> {
  double _sliderValue = 0;

  @override
  void initState() {
    _sliderValue = widget.startValue.h ?? 0;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Wrap(children: [
      Text(widget.label),
      Slider(
        onChangeEnd: (double value) => widget.onChangeEnd(ParamResult(
            paramType: ParamType.ARRAY,
            paramLength: 4,
            value: [value, value, value, value])),
        onChanged: (double value) => setState(() {
          _sliderValue = value;
        }),
        value: _sliderValue,
      )
    ]);
  }
}
