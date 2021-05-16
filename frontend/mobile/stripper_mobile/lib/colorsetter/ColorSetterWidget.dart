import 'package:flutter/material.dart';
import 'package:stripper_mobile/colorsetter/modes/SingleColorPulse.dart';
import 'package:stripper_mobile/colorsetter/modes/SolidColor.dart';
import 'package:stripper_mobile/types/device.dart';
import 'package:tuple/tuple.dart';

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
  List<Tuple2<String, int>> modes = [];
  int selectedChipIndex = 0;

  @override
  void initState() {
    List<Tuple2<String, int>> filteredModes = [];
    for (int i = 0; i < widget.allModes.length; i++) {
      if (widget.device.supported_modes.contains(i)) {
        filteredModes.add(Tuple2<String, int>(widget.allModes[i], i));
      }
    }
    modes = filteredModes;
    if (widget.device.state.mode != null) {
      for (int i = 0; i < modes.length; i++) {
        if (modes[i].item2 == widget.device.state.mode.mode_id) {
          selectedChipIndex = i;
        }
      }
    }
    super.initState();
  }

  Widget _getStateWidget() {
    switch (modes[selectedChipIndex].item2) {
      case 0:
        return SolidColorWidget(device: widget.device);
      case 1:
        return SingleColorPulseWidget(device: widget.device);
      default:
        return Text("MODE2-n + default");
    }
    ;
  }

  @override
  Widget build(BuildContext context) {
    print("BUILDING: " + widget.device.toJson().toString());
    return Scaffold(
        appBar: AppBar(
          title: Text("Set color"),
        ),
        body: SingleChildScrollView(
          scrollDirection: Axis.vertical,
          child: Column(children: [
            SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Padding(
                padding: EdgeInsets.fromLTRB(0, 3, 0, 0),
                child: Wrap(
                  children: List.generate(modes.length, (index) {
                    return Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 2.0),
                      child: ChoiceChip(
                          label: Text(
                            modes[index].item1,
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
            ),
          ]),
        ));
  }
}
