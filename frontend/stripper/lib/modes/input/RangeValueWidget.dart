import 'package:flutter/material.dart';
import 'package:stripper/modes/ModeDefinition.dart';
import 'package:stripper/types/ParamResult.dart';

class RangeValueWidget extends StatefulWidget {
  final ParamResult startValue;
  final String label;
  final ValueChanged<ParamResult> onChangeEnd;

  RangeValueWidget(
      {required this.startValue,
      required this.label,
      required this.onChangeEnd});

  @override
  State<StatefulWidget> createState() => _SingleValueState();
}

class _SingleValueState extends State<RangeValueWidget> {
  double sliderValue = 0;

  @override
  void initState() {
    sliderValue = widget.startValue.value[0];
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      Text(widget.label),
      Slider(
        onChanged: (double value) => setState(() {
          sliderValue = value;
        }),
        onChangeEnd: (value) => widget.onChangeEnd(
            ParamResult(paramLength: 2, paramType: ParamType.ARRAY)),
        value: sliderValue,
      ),
    ]);
  }
}
