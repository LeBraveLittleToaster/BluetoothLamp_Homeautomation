import 'package:flutter/material.dart';
import 'package:stripper_mobile/colorsetter/ColorSetterWidget.dart';
import 'package:stripper_mobile/types/device.dart';

class DeviceSelecterWidget extends StatefulWidget {
  final List<Device> devices;
  const DeviceSelecterWidget({Key key, @required this.devices})
      : super(key: key);

  @override
  State<StatefulWidget> createState() => _DeviceSelecterState();
}

class _DeviceSelecterState extends State<DeviceSelecterWidget> {
  List<Device> devices;

  _onLightbulbClicked(int index) {
    devices[index].state.is_on = !devices[index].state.is_on;
    setState(() {
      devices = List.from(devices);
    });
  }

  @override
  void initState() {
    devices = this.widget.devices;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    devices.forEach((element) => print(element.toJson()));
    return ListView.builder(
        itemCount: devices.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(devices[index].name),
            trailing: IconButton(
                onPressed: () => _onLightbulbClicked(index),
                icon: Icon(devices[index].state.is_on
                    ? Icons.lightbulb
                    : Icons.lightbulb_outline)),
          );
        });
  }
}

