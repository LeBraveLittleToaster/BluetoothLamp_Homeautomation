import 'dart:async';
import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:stripper_mobile/types/device.dart';
import 'package:flutter/foundation.dart' show kIsWeb;

String BASE_URL_ANDROID = "http://10.0.2.2:4321";
String BASE_URL_WEB = "http://localhost:4321";

class Requester {
  static Future<List<Device>> getDeviceList() async {
    var url = (kIsWeb ? BASE_URL_WEB : BASE_URL_ANDROID) + "/device/list";
    var completer = new Completer<List<Device>>();
    http.get(Uri.parse(url),headers: {'Content-Type':'application/json'}).then((response) {
      print(response.body);
      List<dynamic> jsondata = jsonDecode(utf8.decode(response.bodyBytes))["devices"];
      List<Device> devices = jsondata.map((e) => Device.fromJson(e)).toList();
      completer.complete(devices);
    });
    return completer.future;
  }
}
