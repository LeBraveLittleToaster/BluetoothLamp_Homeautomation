import 'dart:convert';

import 'package:stripper_mobile/types/modes.dart';

String buildSetModeJsonStringBody(Mode mode) {
  return json.encode({"mode": mode.toJson()});
}

String buildAddMoodJsonString(String name, List<String> deviceUuids) {
  return json.encode({
    "mood": {"name": name, "device_uuids": deviceUuids}
  });
}
