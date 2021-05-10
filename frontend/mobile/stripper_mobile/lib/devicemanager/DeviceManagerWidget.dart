import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:stripper_mobile/devicemanager/ManageDevice.dart';
import 'package:stripper_mobile/net/requester.dart';
import 'package:stripper_mobile/types/device.dart';

class DeviceManagerWidget extends StatefulWidget {
  final List<Device> devices;
  const DeviceManagerWidget({Key key, @required this.devices})
      : super(key: key);
  @override
  State<StatefulWidget> createState() => new DeviceManagerState();
}

class DeviceManagerState extends State<DeviceManagerWidget> {
  @override
  Widget build(BuildContext context) {
    return ListView.builder(
        itemCount: widget.devices.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(widget.devices[index].name),
            onTap: () => Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) =>
                      ManageDeviceRoute(device: widget.devices[index]),
                )),
          );
        });
  }
}
