import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:stripper/types/ModeDefinition.dart';
import 'package:stripper/modes/ModeWidget.dart';
import 'package:stripper/store/ModeDefinitionModel.dart';
import 'package:stripper/types/device.dart';

class MobileModeWrapperWidget extends StatefulWidget {
  final Device device;
  final String title = "Choose mode";

  MobileModeWrapperWidget({required this.device});

  @override
  State<StatefulWidget> createState() => _MobileModeWrapperState();
}

class _MobileModeWrapperState extends State<MobileModeWrapperWidget> {
  int? selectedModeId;

  @override
  void initState() {
    selectedModeId = widget.device.state?.mode?.modeId;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: NestedScrollView(
            floatHeaderSlivers: true,
            body: Consumer<ModeDefinitionModel>(
                builder: (context, modeModel, child) {
              ModeDefinition? def = getDefinitionById(
                  selectedModeId, modeModel.definitions, widget.device);

              return def == null
                  ? Text("Something went wrong")
                  : Column(
                      children: [
                        ModeWidget(definition: def, device: widget.device)
                      ],
                    );
            }),
            headerSliverBuilder:
                (BuildContext context, bool innerBoxIsScrolled) {
              return [
                SliverAppBar(
                  title: Text(widget.title),
                  pinned: false,
                  floating: true,
                  forceElevated: innerBoxIsScrolled,
                )
              ];
            }));
  }

  ModeDefinition? getDefinitionById(
      int? selectedModeId, List<ModeDefinition> definitions, Device device) {
    int modeId = device.supportedModes?.first ?? 0;
    modeId = selectedModeId ?? modeId;
    try {
      return definitions.firstWhere((element) => element.modeId == modeId);
    } catch (error) {
      print(error);
      return null;
    }
  }
}
