import 'package:flutter/material.dart';
import 'package:stripper/modes/ModeDefinition.dart';
import 'package:stripper/modes/input/HsvBWidget.dart';
import 'package:stripper/modes/input/RangeValueWidget.dart';
import 'package:stripper/modes/input/SingleValueWidget.dart';
import 'package:stripper/modes/net/Requester.dart';
import 'package:stripper/types/ParamResult.dart';
import 'package:stripper/types/device.dart';
import 'package:tuple/tuple.dart';

class ModeWidget extends StatefulWidget {
  final ModeDefinition definition;
  final Map<String, double>? initMode;
  final Device device;

  ModeWidget({required this.definition, this.initMode, required this.device});

  @override
  State<StatefulWidget> createState() => _ModeState(definition: definition);
}

class _ModeState extends State<ModeWidget> {
  final ModeDefinition definition;
  late final List<Tuple2<String, dynamic>> colorWidgetStates;
  late final List<Tuple2<String, dynamic>> modeWidgetStates;

  _ModeState({required this.definition});

  @override
  void initState() {
    this.colorWidgetStates =
        generateColorWidgetStates(definition, widget.initMode);
    this.modeWidgetStates =
        generateModeWidgetStates(definition, widget.initMode);
    print("STATES INIT: " + this.colorWidgetStates.toString());
    super.initState();
  }

  void triggerUploadMode() {
    Requester.setDeviceMode(widget.device.uuid ?? "", definition.modeId ?? -1,
        modeWidgetStates, colorWidgetStates);
    print("Uploading");
  }

  void updateColorState(int index, dynamic value) {
    Tuple2<String, dynamic> oldValue = this.colorWidgetStates.removeAt(index);
    this.colorWidgetStates.insert(
        index, Tuple2<String, dynamic>.fromList([oldValue.item1, value]));
    print("COLOR STATES: " + colorWidgetStates.toString());
    triggerUploadMode();
  }

  void updateModeState(int index, dynamic value) {
    Tuple2<String, dynamic> oldValue = this.modeWidgetStates.removeAt(index);
    this.modeWidgetStates.insert(
        index, Tuple2<String, dynamic>.fromList([oldValue.item1, value]));
    print("MODE STATES: " + modeWidgetStates.toString());
    triggerUploadMode();
  }

  @override
  Widget build(BuildContext context) {
    List<Widget> colorAndModeParamWdigets = [];
    colorAndModeParamWdigets.addAll(
        generateColorParamWidgets(widget.definition, this.updateColorState));
    colorAndModeParamWdigets.addAll(
        generateModeParamWidgets(widget.definition, this.updateModeState));
    return Column(children: colorAndModeParamWdigets);
  }
}

List<Widget> generateModeParamWidgets(ModeDefinition definition,
    void Function(int index, double value) updateModeState) {
  List<Widget> widgets = [];
  int i = 0;
  definition.modeParams?.forEach((element) {
    int elementIndex = i;
    switch (element.modeParamType) {
      case ModeParamType.SINGLE_VALUE:
        widgets
            .add(getSingleValueWidget(elementIndex, element, updateModeState));
        break;
      case ModeParamType.RANGE_VALUE:
        widgets
            .add(getRangeValueWidget(elementIndex, element, updateModeState));
        break;
      default:
        break;
    }
    i++;
  });
  return widgets;
}

Widget getRangeValueWidget(int index, ModeParam modeParam,
    void Function(int index, double value) updateModeState) {
  return RangeValueWidget(
    startValue: 0,
    label: modeParam.label ?? "no label",
    onChangeEnd: (value) => updateModeState(index, value),
  );
}

Widget getSingleValueWidget(int index, ModeParam modeParam,
    void Function(int index, double value) updateModeState) {
  return SingleValueWidget(
    startValue: 0,
    label: modeParam.label ?? "no label",
    onChangeEnd: (value) => updateModeState(index, value),
  );
}

List<Widget> generateColorParamWidgets(ModeDefinition definition,
    void Function(int index, dynamic value) updateColorState) {
  List<Widget> widgets = [];
  int i = 0;
  definition.colorParams?.forEach((element) {
    int i_temp = i;
    switch (element.colorParamType) {
      case ColorParamType.HSV_B:
        widgets.add(HsvBWidget(
          label: element.label ?? "No label given",
          startValue: HsvBValues(h: 0, s: 0, v: 0, b: 0),
          onChangeEnd: (HsvBValues value) => updateColorState(i_temp, value),
        ));
        break;
      default:
        break;
    }
    i++;
  });
  return widgets;
}

List<Tuple2<String, dynamic>> generateColorWidgetStates(
    ModeDefinition definition, Map<String, double>? initMode) {
  List<Tuple2<String, dynamic>> states = [];
  definition.colorParams?.forEach((element) {
    states.add(Tuple2<String, dynamic>.fromList([element.jsonKey, null]));
  });
  return states;
}

List<Tuple2<String, dynamic>> generateModeWidgetStates(
    ModeDefinition definition, Map<String, double>? initMode) {
  List<Tuple2<String, dynamic>> states = [];
  definition.modeParams?.forEach((element) {
    states.add(Tuple2<String, dynamic>.fromList([element.jsonKey, null]));
  });
  return states;
}
