import 'dart:convert';

import 'package:stripper_mobile/types/modes.dart';

String buildSetModeJsonStringBody(Mode mode) {
  return json.encode({
    "mode" : mode.toJson()
  });
}
