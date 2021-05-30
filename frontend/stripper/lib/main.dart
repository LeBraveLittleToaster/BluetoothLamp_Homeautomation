import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:stripper/store/DeviceListModel.dart';
import 'package:stripper/types/ModeDefinition.dart';
import 'package:stripper/modes/ModeWidget.dart';
import 'package:stripper/modes/net/Requester.dart';
import 'package:stripper/store/ModeDefinitionModel.dart';
import 'package:stripper/types/device.dart';
import 'package:stripper/ui/mobile/MobileDeviceListWidget.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
        providers: [
          ChangeNotifierProvider<DeviceListModel>(
            create: (_) => DeviceListModel().initDevices(),
          ),
          ChangeNotifierProvider<ModeDefinitionModel>(
            create: (_) => ModeDefinitionModel().initModeDefinitions(),
          )
        ],
        builder: (context, child) => MaterialApp(
              title: 'Flutter Demo',
              theme: ThemeData.dark(),
              home: MyHomePage(title: 'Flutter Demo Home Page'),
            ));
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: NestedScrollView(
        floatHeaderSlivers: true,
        body: Center(
          child: MobileDeviceListWidget(),
        ),
        headerSliverBuilder: (BuildContext context, bool innerBoxIsScrolled) {
          return [
            SliverAppBar(
              title: Text(widget.title),
              pinned: false,
              floating: true,
              forceElevated: innerBoxIsScrolled,
            )
          ];
        },
      )
    );
  }
}
