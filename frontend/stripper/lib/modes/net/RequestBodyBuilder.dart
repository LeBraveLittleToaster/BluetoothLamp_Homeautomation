import 'dart:convert';

import 'package:stripper/types/ParamValue.dart';
import 'package:tuple/tuple.dart';

String buildSetModeJsonStringBody(
    int modeId,
    List<Tuple2<String, ParamValue>> modeWidgetStates,
    List<Tuple2<String, ParamValue>> colorWidgetStates) {
  return json.encode(
      {"mode": getModeObject(modeId, modeWidgetStates, colorWidgetStates)});
}

dynamic getModeObject(
    int modeId,
    List<Tuple2<String, ParamValue>> modeWidgetStates,
    List<Tuple2<String, ParamValue>> colorWidgetStates) {
  return {
    "mode_id": modeId,
    "color_params": getMapFromStates(colorWidgetStates),
    "mode_params": getMapFromStates(modeWidgetStates)
  };
}

Map<String, ParamValue> getMapFromStates(
    List<Tuple2<String, ParamValue>> state) {
  Map<String, ParamValue> jsonMap = Map<String, ParamValue>();
  state.forEach((element) {
    jsonMap.putIfAbsent(element.item1, () => element.item2);
  });
  return jsonMap;
}

String buildAddMoodJsonString(String name, List<String> deviceUuids) {
  return json.encode({
    "mood": {"name": name, "device_uuids": deviceUuids}
  });
}
