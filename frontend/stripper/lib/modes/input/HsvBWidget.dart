import 'package:flutter/material.dart';
import 'package:stripper/modes/input/CircularColorSelectWidget.dart';
import 'package:stripper/types/ModeDefinition.dart';
import 'package:stripper/types/ParamValue.dart';

class HsvBWidget extends StatefulWidget {
  final String label;
  final ParamValue startValue;
  final ValueChanged<ParamValue> onChangeEnd;

  HsvBWidget(
      {required this.label,
      required this.onChangeEnd,
      required this.startValue});
  @override
  State<StatefulWidget> createState() => _HsvBState();
}

class _HsvBState extends State<HsvBWidget> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(8, 30, 8, 30),
      child: Wrap(runSpacing: 20, children: [
        CircularColorSelectWidget(
          initParam: widget.startValue,
            onColorChanged: (double angle, double brightness) => widget.onChangeEnd(ParamValue(
                paramType: ParamType.ARRAY,
                paramLength: 4,
                value: [angle, 1, 1, brightness])))
      ]),
    );
  }
}
