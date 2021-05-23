import 'dart:async';
import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:http/http.dart';
import 'package:stripper/modes/ModeDefinition.dart';
import 'package:stripper/types/device.dart';
import 'package:stripper/types/mood.dart';
import 'package:tuple/tuple.dart';

import 'RequestBodyBuilder.dart';

String BASE_URL_ANDROID = "http://10.0.2.2:4321";
String BASE_URL_WEB = "http://localhost:4321";

class Requester {
  static Future<List<ModeDefinition>> getModeDefinitions() async {
    var url =
        (kIsWeb ? BASE_URL_WEB : BASE_URL_ANDROID) + "/mode/template/list";
    var completer = new Completer<List<ModeDefinition>>();
    http.get(Uri.parse(url),
        headers: {'Content-Type': 'application/json'}).then((response) {
      print(response.body);
      List<dynamic> jsondata =
          jsonDecode(utf8.decode(response.bodyBytes))["mode_templates"];
      List<ModeDefinition> devices =
          jsondata.map((e) => ModeDefinition.fromJson(e)).toList();
      completer.complete(devices);
    });
    return completer.future;
  }

  static Future<List<Device>> getDeviceList() async {
    var url = (kIsWeb ? BASE_URL_WEB : BASE_URL_ANDROID) + "/device/list";
    var completer = new Completer<List<Device>>();
    http.get(Uri.parse(url),
        headers: {'Content-Type': 'application/json'}).then((response) {
      print(response.body);
      List<dynamic> jsondata =
          jsonDecode(utf8.decode(response.bodyBytes))["devices"];
      List<Device> devices = jsondata.map((e) => Device.fromJson(e)).toList();
      completer.complete(devices);
    });
    return completer.future;
  }

  static Future<List<Mood>> getMoodList() async {
    var url = (kIsWeb ? BASE_URL_WEB : BASE_URL_ANDROID) + "/mood/list";
    var completer = new Completer<List<Mood>>();
    http.get(Uri.parse(url),
        headers: {'Content-Type': 'application/json'}).then((response) {
      print(response.body);
      List<dynamic> jsondata =
          jsonDecode(utf8.decode(response.bodyBytes))["moods"];
      List<Mood> moods = jsondata.map((e) => Mood.fromJson(e)).toList();
      completer.complete(moods);
    });
    return completer.future;
  }

  static void addMood(String name, List<String> deviceUuids) {
    var url = (kIsWeb ? BASE_URL_WEB : BASE_URL_ANDROID) + "/mood/add";
    http
        .put(Uri.parse(url),
            headers: {'Content-Type': 'application/json'},
            body: buildAddMoodJsonString(name, deviceUuids))
        .then((response) {});
  }

  static void setMood(String mood_uuid) async {
    var url = (kIsWeb ? BASE_URL_WEB : BASE_URL_ANDROID) +
        "/mood/" +
        mood_uuid +
        "/set";
    http.get(Uri.parse(url)).then((response) {});
  }

  static void setDeviceMode(
      String deviceUuid, int modeId, List<Tuple2<String, dynamic>> modeWidgetStates, List<Tuple2<String, dynamic>> colorWidgetStates) async {
    var url = (kIsWeb ? BASE_URL_WEB : BASE_URL_ANDROID) +
        "/mode/" +
        deviceUuid +
        "/set";
    http
        .post(Uri.parse(url),
            headers: {'Content-Type': 'application/json'},
            body: buildSetModeJsonStringBody(modeId, modeWidgetStates, colorWidgetStates))
        .then((response) {});
  }

  static void setDeviceIsOn(String device_uuid, bool is_on) async {
    var url = (kIsWeb ? BASE_URL_WEB : BASE_URL_ANDROID) +
        "/device/" +
        device_uuid +
        "/state/set\$is_on=" +
        is_on.toString();
    http.put(Uri.parse(url),
        headers: {'Content-Type': 'application/json'}).then((response) {});
  }

  static Future<Response> deleteMood(String moodUuid) {
    var url = (kIsWeb ? BASE_URL_WEB : BASE_URL_ANDROID) +
        "/mood/" +
        moodUuid +
        "/delete";
    return http.delete(Uri.parse(url));
  }
}
