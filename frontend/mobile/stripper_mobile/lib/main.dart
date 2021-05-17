import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:prompt_dialog/prompt_dialog.dart';
import 'package:stripper_mobile/colorsetter/MoodSetterWidget.dart';
import 'package:stripper_mobile/devicemanager/DeviceSelecterWidget.dart';
import 'package:stripper_mobile/net/requester.dart';
import 'package:stripper_mobile/types/device.dart';

import 'colorsetter/moods/MoodBuilder.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Stripper',
      theme: ThemeData.dark(),
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

  Widget _getWidgetOption(int index) {
    switch (index) {
      case 0:
        return DeviceSelecterWidget();
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
    return Scaffold(
      appBar: AppBar(
        centerTitle: kIsWeb,
        title: kIsWeb
            ? Wrap(
                runSpacing: 20,
                children: [
                  Padding(
                    padding: const EdgeInsets.fromLTRB(30, 0, 30, 0),
                    child: Wrap(runSpacing: 2, children: [
                      IconButton(
                          icon: Icon(Icons.home),
                          onPressed: () => _onItemTapped(0)),
                      Text(
                        "Home",
                        style: TextStyle(fontSize: 12),
                      )
                    ]),
                  ),
                  Padding(
                      padding: const EdgeInsets.fromLTRB(30, 0, 30, 0),
                      child: Wrap(runSpacing: 2, children: [
                        IconButton(
                            icon: Icon(Icons.mood),
                            onPressed: () => _onItemTapped(1)),
                        Text(
                          "Mood",
                          style: TextStyle(fontSize: 12),
                        )
                      ]))
                ],
              )
            : Text("Stripper"),
        actions: [
          IconButton(
              icon: Icon(Icons.add),
              onPressed: _selectedIndex == 0
                  ? () async {
                      addDevicePrompt(context).then((value) => {
                            ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                                content: Text(value == null
                                    ? "No device added..."
                                    : "Device added...")))
                          });
                    }
                  : () => Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) =>
                              MoodBuilderWidget())))
        ],
      ),
      body: Center(
          child: Column(
        children: [
          Expanded(
            child: ConstrainedBox(
                constraints: BoxConstraints(minWidth: 300, maxWidth: 700),
                child: _getWidgetOption(_selectedIndex)),
          ),
        ],
      )),
      bottomNavigationBar: kIsWeb
          ? null
          : BottomNavigationBar(
              items: const <BottomNavigationBarItem>[
                BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
                BottomNavigationBarItem(icon: Icon(Icons.mood), label: "Moods")
              ],
              currentIndex: _selectedIndex,
              selectedItemColor: Colors.amber[800],
              onTap: _onItemTapped,
            ),
    );
  }

  Future<String> addDevicePrompt(BuildContext context) async {
    return prompt(
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
    );
  }
}
