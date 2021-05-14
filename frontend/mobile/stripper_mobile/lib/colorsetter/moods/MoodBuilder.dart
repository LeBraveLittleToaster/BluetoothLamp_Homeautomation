import 'package:flutter/material.dart';
import 'package:stripper_mobile/types/device.dart';

class MoodBuilderWidget extends StatefulWidget {
  final List<Device> devices;
  MoodBuilderWidget({Key key, @required this.devices}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _MoodBuilderState();
}

class _MoodBuilderState extends State<MoodBuilderWidget> {
  List<Device> _selectedItems = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text("Create Mood")),
        body: Center(
          child: Column(
            children: [
              Expanded(
                child: ConstrainedBox(
                  constraints: BoxConstraints(minWidth: 300, maxWidth: 700),
                  child: ListView.builder(
                    itemCount: widget.devices.length,
                    itemBuilder: (context, index) {
                      return ListTile(title: Text(widget.devices[index].name));
                    },
                  ),
                ),
              ),
            ],
          ),
        ));
  }
}
