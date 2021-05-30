import 'package:flutter/foundation.dart';
import 'package:stripper/modes/net/Requester.dart';
import 'package:stripper/types/ParamValue.dart';
import 'package:stripper/types/device.dart';
import 'package:tuple/tuple.dart';

class DeviceListModel extends ChangeNotifier {
  List<Device> devices = [];
  bool _isLoading = false;
  bool get isLoading {
    return _isLoading;
  }

  DeviceListModel initDevices() {
    loadDevices();
    return this;
  }

  void loadDevices() {
    _isLoading = true;
    notifyListeners();
    Requester.getDeviceList().then((value) {
      devices = value;
      _isLoading = false;
      notifyListeners();
    }).catchError((error) {
      print(error);
      _isLoading = false;
      notifyListeners();
    });
  }

  void setStateIsOn(String deviceId, bool isOn) {
    Device device = devices.firstWhere((element) => element.uuid == deviceId);
    device.state?.isOn = isOn;
    notifyListeners();
  }

  void setDeviceMode(
      String? uuid,
      int? modeId,
      List<Tuple2<String, ParamValue>> modeWidgetStates,
      List<Tuple2<String, ParamValue>> colorWidgetStates) {
    Requester.setDeviceMode(
        uuid ?? "", modeId ?? -1, modeWidgetStates, colorWidgetStates);
  }
}
