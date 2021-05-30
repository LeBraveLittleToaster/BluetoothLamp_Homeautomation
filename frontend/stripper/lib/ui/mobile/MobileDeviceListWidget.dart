import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:provider/provider.dart';
import 'package:stripper/DataStore.dart';

class MobileDeviceListWidget extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _MobileDeviceListState();
}

class _MobileDeviceListState extends State<MobileDeviceListWidget> {
  @override
  Widget build(BuildContext context) {
    return Consumer<DeviceListModel>(builder: (context, deviceModel, child) {
      print("Rebuilding");
      return deviceModel.isLoading
          ? SpinKitCubeGrid(
            color: Colors.orangeAccent,
          )
          : Text("Loaded " + (deviceModel.devices.length).toString() + " devices");
    });
  }
}
