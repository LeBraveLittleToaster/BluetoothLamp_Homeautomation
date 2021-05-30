import 'package:flutter/material.dart';
import 'package:stripper/types/ModeDefinition.dart';
import 'package:stripper/types/ParamValue.dart';

class RangeValueWidget extends StatefulWidget {
  final ParamValue startValue;
  final String label;
  final ValueChanged<ParamValue> onChangeEnd;

  RangeValueWidget(
      {required this.startValue,
      required this.label,
      required this.onChangeEnd});

  @override
  State<StatefulWidget> createState() => _RangeValueState();
}

class _RangeValueState extends State<RangeValueWidget> {
  RangeValues sliderValues = RangeValues(0, 0);

  @override
  void initState() {
    dynamic v1 = widget.startValue.value?[0] ?? 0;
    dynamic v2 = widget.startValue.value?[1] ?? 1;
    sliderValues = RangeValues(v1?.toDouble() ?? 0, v2?.toDouble() ?? 0);
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      Text(widget.label),
      RangeSlider(
        onChanged: (RangeValues value) => setState(() {
          sliderValues = value;
        }),
        onChangeEnd: (value) => widget.onChangeEnd(ParamValue(
            paramLength: 2,
            paramType: ParamType.ARRAY,
            value: [sliderValues.start, sliderValues.end])),
        values: sliderValues,
      ),
    ]);
  }
}
