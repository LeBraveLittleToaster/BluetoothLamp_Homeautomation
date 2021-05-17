import 'package:flutter/material.dart';
import 'package:stripper_mobile/types/device.dart';

class ManageDeviceRoute extends StatefulWidget {
  final Device device;
  const ManageDeviceRoute({Key key, @required this.device}) : super(key: key);

  @override
  State<StatefulWidget> createState() => new ManageDeviceState();
}

class ManageDeviceState extends State<ManageDeviceRoute> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Change Device"),
      ),
      body: Center(
        child: Text(widget.device.name),
      ),
    );
  }
}
