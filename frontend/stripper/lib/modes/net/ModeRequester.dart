import 'dart:async';
import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:http/http.dart';
import 'package:stripper/modes/GenericModeDefinition.dart';


String BASE_URL_ANDROID = "http://10.0.2.2:4321";
String BASE_URL_WEB = "http://localhost:4321";

class ModeRequester {
  static Future<List<GenericModeDefinition>> getModeDefinitions() async {
    var url = (kIsWeb ? BASE_URL_WEB : BASE_URL_ANDROID) + "/mode/template/list";
    var completer = new Completer<List<GenericModeDefinition>>();
    http.get(Uri.parse(url),
        headers: {'Content-Type': 'application/json'}).then((response) {
      print(response.body);
      List<dynamic> jsondata =
          jsonDecode(utf8.decode(response.bodyBytes))["mode_templates"];
      List<GenericModeDefinition> devices = jsondata.map((e) => GenericModeDefinition.fromJson(e)).toList();
      completer.complete(devices);
    });
    return completer.future;
  }
}
