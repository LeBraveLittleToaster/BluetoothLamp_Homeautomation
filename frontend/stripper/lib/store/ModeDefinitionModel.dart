import 'package:flutter/foundation.dart';
import 'package:stripper/types/ModeDefinition.dart';
import 'package:stripper/modes/net/Requester.dart';

class ModeDefinitionModel extends ChangeNotifier {
  List<ModeDefinition> definitions = [];
  bool _isLoading = false;
  bool get isLoading {
    return _isLoading;
  }

  ModeDefinitionModel initModeDefinitions(){
    loadModeDefinitions();
    return this;
  }

  void loadModeDefinitions() {
    _isLoading = true;
    notifyListeners();
    Requester.getModeDefinitions().then((value) {
      definitions = value;
      _isLoading = false;
      notifyListeners();
    }).catchError((error) {
      print(error);
      _isLoading = false;
      notifyListeners();
    });
  }
}
