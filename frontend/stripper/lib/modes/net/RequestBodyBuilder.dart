import 'dart:convert';

import 'package:tuple/tuple.dart';

String buildSetModeJsonStringBody(int modeId,
    List<Tuple2<String, dynamic>> modeWidgetStates,
    List<Tuple2<String, dynamic>> colorWidgetStates) {
  var mode = {
    "mode_id" : modeId,
    "color_params": getMapFromStates(colorWidgetStates),
    "mode_params": getMapFromStates(modeWidgetStates)
  };
  return json.encode({"mode": mode});
}

Map<String, dynamic> getMapFromStates(List<Tuple2<String, dynamic>> state) {
  Map<String, dynamic> jsonMap = Map<String, dynamic>();
  state.forEach((element) {
    jsonMap.putIfAbsent(element.item1, () => element.item2 ?? 0);
  });
  return jsonMap;
}

String buildAddMoodJsonString(String name, List<String> deviceUuids) {
  return json.encode({
    "mood": {"name": name, "device_uuids": deviceUuids}
  });
}
