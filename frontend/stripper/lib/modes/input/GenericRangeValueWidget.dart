import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

class GenericSingleValueWidget extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _GenericSingleValueState();
}

class _GenericSingleValueState extends State<GenericSingleValueWidget> {
  @override
  Widget build(BuildContext context) {
    return Slider(
      onChanged: (double value) {},
      value: 0,
    );
  }
}
