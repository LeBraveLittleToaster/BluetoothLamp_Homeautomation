import 'package:flutter/widgets.dart';
import 'package:stripper/modes/GenericModeDefinition.dart';
import 'package:stripper/modes/input/GenericHsvBWidget.dart';
import 'package:tuple/tuple.dart';

class GenericModeWidget extends StatefulWidget {
  final GenericModeDefinition definition;

  GenericModeWidget({required this.definition});

  @override
  State<StatefulWidget> createState() =>
      _GenericModeState(definition: definition);
}

class _GenericModeState extends State<GenericModeWidget> {
  final GenericModeDefinition definition;
  late final List<Tuple2<String, String?>> colorWidgetStates;

  _GenericModeState({required this.definition});

  @override
  void initState() {
    this.colorWidgetStates = generateColorWidgetStates(definition);
    print("STATES INIT: " + this.colorWidgetStates.toString());
    super.initState();
  }

  void updateState(int index, String value) {
    Tuple2<String, String?> oldValue = this.colorWidgetStates.removeAt(index);
    this.colorWidgetStates.insert(
        index, Tuple2<String, String>.fromList([oldValue.item1, value]));
    print("STATES: " + colorWidgetStates.toString());
  }

  @override
  Widget build(BuildContext context) {
    return Column(
        children:
            generateColorParamWidgets(widget.definition, this.updateState));
  }
}

List<Widget> generateColorParamWidgets(GenericModeDefinition definition,
    void Function(int index, String value) updateState) {
  List<Widget> widgets = [];
  int i = 0;
  definition.colorParams?.forEach((element) {
    int i_temp = i;
    switch (element.colorParamType) {
      case ColorParamType.HSV_B:
        widgets.add(GenericHsvBWidget(
          label: element.label ?? "No label given",
          startValue: 0,
          onChangeEnd: (double value) => updateState(i_temp, value.toString()),
        ));
        break;
      default:
        break;
    }
    i++;
  });
  return widgets;
}

List<Tuple2<String, String?>> generateColorWidgetStates(
    GenericModeDefinition definition) {
  List<Tuple2<String, String?>> states = [];
  definition.colorParams?.forEach((element) {
    states.add(Tuple2<String, String?>.fromList([element.jsonKey, null]));
  });
  return states;
}
