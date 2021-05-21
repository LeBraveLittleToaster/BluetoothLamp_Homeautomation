import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:provider/provider.dart';
import 'package:stripper_mobile/colorsetter/ColorSetterWidget.dart';
import 'package:stripper_mobile/net/requester.dart';
import 'package:stripper_mobile/types/device.dart';

import 'ManageDevice.dart';

_DeviceSelecterState state;

class DeviceSelecterWidget extends StatefulWidget {
  const DeviceSelecterWidget({Key key}) : super(key: key);

  @override
  State<StatefulWidget> createState() {
    state = _DeviceSelecterState();
    return state;
  }
}

class _DeviceSelecterState extends State<DeviceSelecterWidget> {
  @override
  Widget build(BuildContext context) {

    FutureProvider<List<Device>>(create: create, initialData: initialData)

    /*
    return FutureBuilder(
      future: Requester.getDeviceList(),
      builder: (context, snapshot) {
        return !snapshot.hasData
            ? Center(
                child: SpinKitCubeGrid(
                  color: Colors.amber,
                ),
              )
            : ListView.builder(
                itemBuilder: (context, index) {
                  return DeviceSelecterListItemWidget(
                    device: snapshot.data[index],
                    onRefreshList: () => setState(() {
                      print("Refreshing List");
                    }),
                  );
                },
                itemCount: snapshot.data.length);
      },
    );*/
  }
}

class DeviceSelecterListItemWidget extends StatefulWidget {
  final Device device;
  final VoidCallback onRefreshList;
  const DeviceSelecterListItemWidget(
      {Key key, @required this.device, @required this.onRefreshList})
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
              )).then((_) => widget.onRefreshList());
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
