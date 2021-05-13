import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:stripper_mobile/colorsetter/ColorSetterWidget.dart';
import 'package:stripper_mobile/net/requester.dart';
import 'package:stripper_mobile/types/device.dart';

import 'ManageDevice.dart';

class DeviceSelecterWidget extends StatelessWidget {
  final List<Device> devices;
  const DeviceSelecterWidget({Key key, @required this.devices})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
        itemBuilder: (context, index) {
          return DeviceSelecterListItemWidget(device: devices[index]);
        },
        itemCount: devices.length);
  }
}

class DeviceSelecterListItemWidget extends StatefulWidget {
  final Device device;

  const DeviceSelecterListItemWidget({Key key, @required this.device})
      : super(key: key);
  @override
  State<StatefulWidget> createState() => _DeviceSelecterListItemState();
}

class _DeviceSelecterListItemState extends State<DeviceSelecterListItemWidget> {
  Device device;

  _onLightbulbClicked() {
    setState(() {
      device.state.is_on = !device.state.is_on;
    });
    Requester.setDeviceIsOn(device.uuid, device.state.is_on);
  }

  @override
  void initState() {
    device = this.widget.device;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return ListTile(
        title: Text(device.name),
        onLongPress: kIsWeb
            ? null
            : () => Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context) => ManageDeviceRoute(device: device))),
        onTap: () {
          Navigator.push(
              context,
              MaterialPageRoute(
                builder: (context) => ColorSetterWidget(device: device),
              ));
        },
        trailing: kIsWeb
            ? Wrap(
                spacing: 12,
                children: [
                  IconButton(
                      onPressed: () => Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) =>
                                  ManageDeviceRoute(device: device))),
                      icon: Icon(Icons.settings)),
                  IconButton(
                      onPressed: () => _onLightbulbClicked(),
                      icon: Icon(device.state.is_on
                          ? Icons.lightbulb
                          : Icons.lightbulb_outline)),
                ],
              )
            : IconButton(
                onPressed: () => _onLightbulbClicked(),
                icon: Icon(device.state.is_on
                    ? Icons.lightbulb
                    : Icons.lightbulb_outline)));
  }
}
