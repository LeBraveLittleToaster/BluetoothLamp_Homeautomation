import 'package:flutter/material.dart';
import 'package:sleek_circular_slider/sleek_circular_slider.dart';
import 'package:stripper_mobile/types/device.dart';

class ColorSetterWidget extends StatefulWidget {
  final List<Device> devices;

  const ColorSetterWidget({Key key, @required this.devices}) : super(key: key);

  @override
  State<StatefulWidget> createState() => new _ColorSetterState();
}

class _ColorSetterState extends State<ColorSetterWidget> {
  Device _dropdownValue;
  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.start,
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(20, 5, 20, 5),
          child: DropdownButton<Device>(
            isExpanded: true,
            value: _dropdownValue,
            icon: Icon(Icons.device_hub),
            onChanged: (Device newValue) {
              setState(() {
                _dropdownValue = newValue;
              });
            },
            items: widget.devices.map((Device device) {
              return new DropdownMenuItem<Device>(
                  value: device, child: Text(device.name));
            }).toList(),
          ),
        ),
        SleekCircularSlider(
          appearance: CircularSliderAppearance(
              customWidths: CustomSliderWidths(
                  progressBarWidth: 40,
                  handlerSize: 30,
                  shadowWidth: 0,
                  trackWidth: 20),
              customColors: CustomSliderColors(progressBarColors: [
                Colors.grey,
                Colors.grey,
              ], trackColors: [
                Colors.grey,
                Colors.grey,
              ]),
              size: MediaQuery.of(context).size.width * 0.8),
          min: 0,
          max: 255,
          initialValue: 0,
          onChangeStart: (double startValue) {
            // callback providing a starting value (when a pan gesture starts)
          },
          onChangeEnd: (double endValue) {
            // ucallback providing an ending value (when a pan gesture ends)
          },
        )
      ],
    );
  }
}
