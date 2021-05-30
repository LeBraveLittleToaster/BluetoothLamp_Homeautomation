import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:provider/provider.dart';
import 'package:stripper/store/DeviceListModel.dart';
import 'package:stripper/types/device.dart';
import 'package:stripper/ui/mobile/MobileModeWrapperWidget.dart';

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
          : ListView.builder(
              itemCount: deviceModel.devices.length,
              itemBuilder: (context, index) =>
                  getListTile(deviceModel.devices[index]));
    });
  }

  ListTile getListTile(Device device) {
    String? deviceUuid = device.uuid;
    String name = device.name ?? "No Device name...";
    bool? isOn = device.state?.isOn;
    return ListTile(
      onTap: () => Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => MobileModeWrapperWidget(device: device),
          )),
      title: Text(name),
      trailing: IconButton(
        icon: Icon(isOn != null
            ? (isOn ? Icons.lightbulb : Icons.lightbulb_outline)
            : Icons.error),
        onPressed: () => deviceUuid == null || isOn == null
            ? null
            : context.read<DeviceListModel>().setStateIsOn(deviceUuid, !isOn),
      ),
    );
  }
}
