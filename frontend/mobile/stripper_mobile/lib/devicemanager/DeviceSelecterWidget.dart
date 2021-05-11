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

class _DeviceSelecterState extends State<DeviceSelecterWidget>{

  @override
  Widget build(BuildContext context) {
    return GridView.builder(
        itemCount: widget.devices.length,
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
        ),
        itemBuilder: (BuildContext context, int index) {
          return GestureDetector(
            onTap: () => Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context) =>
                        ColorSetterWidget(device: widget.devices[index]))),
            child: new Card(
              child: new GridTile(
                  footer: new Text(widget.devices[index].name),
                  child: Padding(
                    padding: const EdgeInsets.all(50.0),
                    child: ElevatedButton(
                      onPressed: () {},
                      child: Icon(
                        Icons.lightbulb,
                        color: Colors.white,
                        size: 60.0,
                      ),
                      style: ElevatedButton.styleFrom(
                          shape: CircleBorder(), primary: Colors.green),
                    ),
                  )
                  //new IconButton(icon: Icon(Icons.lightbulb), onPressed: () {}),
                  ),
            ),
          );
        });
  }
}
