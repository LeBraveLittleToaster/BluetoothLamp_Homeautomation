import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:prompt_dialog/prompt_dialog.dart';
import 'package:stripper_mobile/colorsetter/MoodSetterWidget.dart';
import 'package:stripper_mobile/devicemanager/DeviceSelecterWidget.dart';
import 'package:stripper_mobile/net/requester.dart';
import 'package:stripper_mobile/types/device.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Stripper'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  List<Device> devices = [];

  int _selectedIndex = 0;
  static const TextStyle optionStyle =
      TextStyle(fontSize: 30, fontWeight: FontWeight.bold);

  Widget _getWidgetOption(int index, List<Device> devices) {
    switch (index) {
      case 0:
        return DeviceSelecterWidget(devices: devices);
      default:
        return MoodSetterWidget();
    }
  }

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
        future: Requester.getDeviceList(),
        builder: (context, snapshot) {
          return !snapshot.hasData
              ? Scaffold(
                  body: Center(
                    child: SpinKitCubeGrid(
                      color: Colors.amber,
                    ),
                  ),
                )
              : Scaffold(
                  appBar: AppBar(
                    title: Text(widget.title),
                    actions: [
                      IconButton(
                        icon: Icon(Icons.add),
                        onPressed: 
                        _selectedIndex == 0 ?
                        () async {
                          return await addDevicePrompt(context);
                        } : () => Navigator.push(context, route)
                      )
                    ],
                  ),
                  body: Center(
                      child: Column(
                    children: [
                      Expanded(
                        child: ConstrainedBox(
                            constraints:
                                BoxConstraints(minWidth: 300, maxWidth: 700),
                            child: _getWidgetOption(
                                _selectedIndex, snapshot.data)),
                      ),
                    ],
                  )),
                  bottomNavigationBar: BottomNavigationBar(
                    items: const <BottomNavigationBarItem>[
                      BottomNavigationBarItem(
                          icon: Icon(Icons.home), label: "Home"),
                      BottomNavigationBarItem(
                          icon: Icon(Icons.mood), label: "Moods")
                    ],
                    currentIndex: _selectedIndex,
                    selectedItemColor: Colors.amber[800],
                    onTap: _onItemTapped,
                  ),
                );
        });
  }

  Future<void> addDevicePrompt(BuildContext context) async {
    return print(await prompt(
                          context,
                          title: Text("Add device uuid.."),
                          initialValue: '',
                          textOK: Text('Yes'),
                          textCancel: Text('No'),
                          hintText: 'Please add uuid...',
                          minLines: 1,
                          maxLines: 3,
                          autoFocus: true,
                          obscureText: false,
                        ));
  }
}
