import 'package:flutter/material.dart';
import 'package:stripper_mobile/types/device.dart';

class ColorSetterWidget extends StatefulWidget {
  final Device device;
  const ColorSetterWidget({Key key, @required this.device}) : super(key: key);

  @override
  State<StatefulWidget> createState() => new _ColorSetterState();
}

class _ColorSetterState extends State<ColorSetterWidget> {
  int _dropdownValue;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(20, 5, 20, 5),
            child: Row(children: [],)
          ),
        ],
      ),
    );
  }
}
