import 'package:flutter/foundation.dart';
import 'package:stripper/modes/net/Requester.dart';
import 'package:stripper/types/device.dart';

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
}
