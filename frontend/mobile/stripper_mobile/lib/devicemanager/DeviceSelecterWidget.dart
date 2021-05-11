import 'package:flutter/material.dart';
import 'package:stripper_mobile/colorsetter/ColorSetterWidget.dart';
import 'package:stripper_mobile/types/device.dart';

class DeviceSelecterWidget extends StatelessWidget {
  final List<Device> devices;
  const DeviceSelecterWidget({Key key, @required this.devices})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GridView.builder(
        itemCount: devices.length,
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
        ),
        itemBuilder: (BuildContext context, int index) {
          return GestureDetector(
            onTap: () => Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context) => ColorSetterWidget(device: devices[index]))),
            child: new Card(
              child: new GridTile(
                footer: new Text(devices[index].name),
                child: new Text(devices[index].uuid),
              ),
            ),
          );
        });
  }
}
