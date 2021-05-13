import 'package:flutter/material.dart';
import 'package:stripper_mobile/colorsetter/modes/SolidColor.dart';
import 'package:stripper_mobile/types/device.dart';

class ColorSetterWidget extends StatefulWidget {
  final List<String> allModes = [
    "Mode0",
    "Mode1",
    "Mode2",
    "Mode3",
    "Mode4",
    "Mode5",
    "Mode6"
  ];
  final Device device;
  ColorSetterWidget({Key key, @required this.device}) : super(key: key);

  @override
  State<StatefulWidget> createState() => new _ColorSetterState();
}

class _ColorSetterState extends State<ColorSetterWidget> {
  List<String> modes = [];
  int selectedChipIndex = 0;

  @override
  void initState() {
    List<String> filteredModes = [];
    for (int i = 0; i < widget.allModes.length; i++) {
      if (widget.device.supported_modes.contains(i)) {
        filteredModes.add(widget.allModes[i]);
      }
    }
    modes = filteredModes;
    super.initState();
  }

  Widget _getStateWidget() {
    switch (selectedChipIndex) {
      case 0:
        return SolidColorWidget(device: widget.device);
      case 1:
        return Text("MODE1");
      default:
        return Text("MODE2-n + default");
    }
    ;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Set color"),
        ),
        body: Column(children: [
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Padding(
              padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
              child: Wrap(
                children: List.generate(modes.length, (index) {
                  return Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 2.0),
                    child: ChoiceChip(
                        label: Text(
                          modes[index],
                          style: Theme.of(context)
                              .textTheme
                              .bodyText2
                              .copyWith(color: Colors.white, fontSize: 14),
                        ),
                        labelPadding: EdgeInsets.all(2.0),
                        selectedColor: Colors.deepOrange,
                        padding: EdgeInsets.symmetric(horizontal: 10),
                        onSelected: (value) {
                          setState(() {
                            selectedChipIndex =
                                value ? index : selectedChipIndex;
                          });
                        },
                        selected: selectedChipIndex == index),
                  );
                }),
              ),
            ),
          ),
          Center(
            child: _getStateWidget(),
          )
        ]));
  }
}
