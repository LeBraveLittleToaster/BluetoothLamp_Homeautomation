import 'package:flutter/material.dart';
import 'package:stripper/types/ModeDefinition.dart';
import 'package:stripper/types/ParamValue.dart';

class SingleValueWidget extends StatefulWidget {
  final ParamValue startValue;
  final String label;
  final ValueChanged<ParamValue> onChangeEnd;

  SingleValueWidget(
      {required this.startValue,
      required this.label,
      required this.onChangeEnd});

  @override
  State<StatefulWidget> createState() => _SingleValueState();
}

class _SingleValueState extends State<SingleValueWidget> {
  double sliderValue = 0;

  @override
  void initState() {
    if (widget.startValue.paramType != ParamType.EMPTY) {
      dynamic v = widget.startValue.value;
      sliderValue = v?.toDouble() ?? 0;
    }
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(widget.label),
        Slider(
          onChanged: (double value) => setState(() {
            sliderValue = value;
          }),
          onChangeEnd: (value) => widget.onChangeEnd(ParamValue(
              paramLength: 1, paramType: ParamType.SINGLE_VALUE, value: value)),
          value: sliderValue,
        ),
      ],
    );
  }
}
