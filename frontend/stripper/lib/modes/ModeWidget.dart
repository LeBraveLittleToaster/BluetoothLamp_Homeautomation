import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:stripper/types/ModeDefinition.dart';
import 'package:stripper/modes/input/HsvBWidget.dart';
import 'package:stripper/modes/input/RangeValueWidget.dart';
import 'package:stripper/modes/input/SingleValueWidget.dart';
import 'package:stripper/store/DeviceListModel.dart';
import 'package:stripper/types/ParamValue.dart';
import 'package:stripper/types/device.dart';
import 'package:tuple/tuple.dart';

class ModeWidget extends StatefulWidget {
  final ModeDefinition definition;
  late final Mode? initMode;
  final Device device;

  ModeWidget({required this.definition, required this.device}) {
    this.initMode = this.device.state?.mode;
  }

  @override
  State<StatefulWidget> createState() => _ModeState();
}

class _ModeState extends State<ModeWidget> {
  late List<Tuple2<String, ParamValue>> colorWidgetStates;
  late List<Tuple2<String, ParamValue>> modeWidgetStates;


  @override
  void initState() {
    generateStates();
    super.initState();
  }

  @override
  void didUpdateWidget(covariant ModeWidget oldWidget) {
    generateStates();
    super.didUpdateWidget(oldWidget);
  }

  void generateStates(){
    print("Generating states");
    this.colorWidgetStates =
        generateColorWidgetStates(widget.definition, widget.initMode);
    this.modeWidgetStates =
        generateModeWidgetStates(widget.definition, widget.initMode);
  }

  void triggerUploadMode() {
    context.read<DeviceListModel>().setDeviceMode(widget.device.uuid ?? "",
        widget.definition.modeId ?? -1, modeWidgetStates, colorWidgetStates);
  }

  void updateColorState(int index, ParamValue value) {
    Tuple2<String, ParamValue> oldValue =
        this.colorWidgetStates.removeAt(index);
    this.colorWidgetStates.insert(
        index, Tuple2<String, ParamValue>.fromList([oldValue.item1, value]));
    triggerUploadMode();
  }

  void updateModeState(int index, ParamValue value) {
    Tuple2<String, ParamValue> oldValue = this.modeWidgetStates.removeAt(index);
    this.modeWidgetStates.insert(
        index, Tuple2<String, ParamValue>.fromList([oldValue.item1, value]));
    triggerUploadMode();
  }

  @override
  Widget build(BuildContext context) {
    return Consumer<DeviceListModel>(builder: (context, modeModel, child) {
      List<Widget> colorAndModeParamWdigets = [];
      colorAndModeParamWdigets.addAll(generateColorParamWidgets(
          widget.definition, colorWidgetStates, this.updateColorState));
      colorAndModeParamWdigets.addAll(generateModeParamWidgets(
          widget.definition, modeWidgetStates, this.updateModeState));
      return Column(children: colorAndModeParamWdigets);
    });
  }
}

List<Widget> generateModeParamWidgets(
    ModeDefinition definition,
    List<Tuple2<String, ParamValue>> modeParamStates,
    void Function(int index, ParamValue value) updateModeState) {
  List<Widget> widgets = [];
  int i = 0;
  definition.modeParams?.forEach((element) {
    int elementIndex = i;
    ParamValue? initValue = modeParamStates[elementIndex].item2;
    switch (element.modeParamType) {
      case ModeParamType.SINGLE_VALUE:
        widgets.add(getSingleValueWidget(
            elementIndex, element, initValue, updateModeState));
        break;
      case ModeParamType.RANGE_VALUE:
        widgets.add(getRangeValueWidget(
            elementIndex, element, initValue, updateModeState));
        break;
      default:
        break;
    }
    i++;
  });
  return widgets;
}

Widget getRangeValueWidget(
    int index,
    ModeParam modeParam,
    ParamValue? initValue,
    void Function(int index, ParamValue value) updateModeState) {
  return RangeValueWidget(
    startValue: initValue ??
        ParamValue(paramLength: 2, paramType: ParamType.ARRAY, value: [0, 1]),
    label: modeParam.label ?? "no label",
    onChangeEnd: (value) => updateModeState(index, value),
  );
}

Widget getSingleValueWidget(
    int index,
    ModeParam modeParam,
    ParamValue? initValue,
    void Function(int index, ParamValue value) updateModeState) {
  return SingleValueWidget(
    startValue: initValue ??
        ParamValue(paramType: ParamType.SINGLE_VALUE, value: 0, paramLength: 1),
    label: modeParam.label ?? "no label",
    onChangeEnd: (value) => updateModeState(index, value),
  );
}

List<Widget> generateColorParamWidgets(
    ModeDefinition definition,
    List<Tuple2<String, ParamValue>> colorStates,
    void Function(int index, ParamValue value) updateColorState) {
  List<Widget> widgets = [];
  int i = 0;
  definition.colorParams?.forEach((element) {
    int elementIndex = i;
    ParamValue? initValue = colorStates[elementIndex].item2;
    switch (element.colorParamType) {
      case ColorParamType.HSV_B:
        widgets.add(HsvBWidget(
          label: element.label ?? "No label given",
          startValue: initValue,
          onChangeEnd: (ParamValue value) =>
              updateColorState(elementIndex, value),
        ));
        break;
      default:
        break;
    }
    i++;
  });
  return widgets;
}

List<Tuple2<String, ParamValue>> generateColorWidgetStates(
    ModeDefinition definition, Mode? initMode) {
  List<Tuple2<String, ParamValue>> states = [];

  definition.colorParams?.forEach((element) {
    ParamValue? initValue = initMode?.colorValues
            ?.firstWhere((initElement) => element.jsonKey == initElement.item1)
            .item2 ??
        null;
    states.add(Tuple2<String, ParamValue>.fromList([
      element.jsonKey,
      initValue ?? ParamValue(paramType: ParamType.EMPTY, paramLength: 0)
    ]));
  });
  return states;
}

List<Tuple2<String, ParamValue>> generateModeWidgetStates(
    ModeDefinition definition, Mode? initMode) {
  List<Tuple2<String, ParamValue>> states = [];
  definition.modeParams?.forEach((element) {
    ParamValue? initValue;
    try {
      initValue = initMode?.modeValues
          ?.firstWhere((initElement) => element.jsonKey == initElement.item1)
          .item2;
    } catch (e) {
      print(e.toString());
    }
    states.add(Tuple2<String, ParamValue>.fromList([
      element.jsonKey,
      initValue ?? ParamValue(paramType: ParamType.EMPTY, paramLength: 0)
    ]));
  });
  return states;
}
