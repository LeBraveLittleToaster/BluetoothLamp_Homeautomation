import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:stripper_mobile/devicemanager/ManageDevice.dart';
import 'package:stripper_mobile/net/requester.dart';
import 'package:stripper_mobile/types/device.dart';

class DeviceManagerWidget extends StatefulWidget {
  const DeviceManagerWidget({
    Key key,
  }) : super(key: key);
  @override
  State<StatefulWidget> createState() => new DeviceManagerState();
}

class DeviceManagerState extends State<DeviceManagerWidget> {
  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<Device>>(
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return ListView.builder(
            itemCount: snapshot.data.length,
            itemBuilder: (context, index) {
              return ListTile(
                title: Text(snapshot.data[index].name),
                onTap: () => Navigator.push(context,
                MaterialPageRoute(builder: (context) => ManageDeviceRoute(device: snapshot.data[index]),)),
              );
            },
          );
        } else {
          return SpinKitThreeBounce(
            color: Colors.grey,
            size: 30.0
          );
        }
      },
      future: Requester.getDeviceList(),
    );
  }
}
