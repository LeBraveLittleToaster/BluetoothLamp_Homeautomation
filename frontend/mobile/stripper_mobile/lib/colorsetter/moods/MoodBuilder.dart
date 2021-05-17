import 'package:flutter/material.dart';
import 'package:flutter_slidable/flutter_slidable.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:prompt_dialog/prompt_dialog.dart';
import 'package:stripper_mobile/net/requester.dart';
import 'package:stripper_mobile/types/device.dart';

class MoodBuilderWidget extends StatefulWidget {
  MoodBuilderWidget({Key key}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _MoodBuilderState();
}

class _MoodBuilderState extends State<MoodBuilderWidget> {
  List<Device> devices;
  List<int> _selectedItems = [];

  @override
  void initState() {
    super.initState();
    Requester.getDeviceList().then((value) => setState(() => devices = value));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Choose Devices..."),
          actions: [
            IconButton(
                icon: Icon(Icons.check),
                onPressed: _selectedItems.length == 0
                    ? null
                    : () async {
                        prompt(
                          context,
                          title: Text("Add mood name..."),
                          initialValue: '',
                          textOK: Text('Submit'),
                          textCancel: Text('Abort'),
                          hintText: 'Please add name...',
                          minLines: 1,
                          maxLines: 3,
                          autoFocus: true,
                          obscureText: false,
                        ).then((value) {
                          if (value == null || value.length > 0) {
                            List<String> d_uuids = [];
                            _selectedItems.forEach((i) {
                              d_uuids.add(devices[i].uuid);
                            });
                            print("VALUE: " + value);
                            Requester.addMood(value, d_uuids);

                            ScaffoldMessenger.of(context).showSnackBar(
                                SnackBar(content: Text("Created new mood...")));

                            Navigator.pop(context);
                          } else {
                            print("No name selected");
                          }
                        }).onError((error, stackTrace) {
                          print(error);
                        });
                      })
          ],
        ),
        body: devices == null
            ? Center(child: SpinKitCubeGrid(color: Colors.amber))
            : Column(
                children: [
                  Expanded(
                    child: Center(
                      child: ConstrainedBox(
                        constraints:
                            BoxConstraints(minWidth: 300, maxWidth: 700),
                        child: ListView.builder(
                          itemCount: devices.length,
                          itemBuilder: (context, index) {
                            return ListTile(
                              title: Text(devices[index].name),
                              trailing: IconButton(
                                onPressed: () {
                                  setState(() {
                                    if (_selectedItems.contains(index)) {
                                      _selectedItems.remove(index);
                                    } else {
                                      _selectedItems.add(index);
                                    }
                                  });
                                },
                                icon: Icon(_selectedItems.contains(index)
                                    ? Icons.check_box_outlined
                                    : Icons.check_box_outline_blank_rounded),
                              ),
                            );
                          },
                        ),
                      ),
                    ),
                  ),
                ],
              ));
  }
}
