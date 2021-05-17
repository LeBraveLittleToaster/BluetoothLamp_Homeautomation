import 'package:stripper_mobile/types/modes.dart';

class DeviceState {
  DeviceState({this.is_on, this.mode});

  bool is_on;
  Mode mode;

  factory DeviceState.fromJson(Map<String, dynamic> json) => DeviceState(
    is_on: json["is_on"],
    mode: json["c_mode"] == null ? null : Mode.fromJson(json["c_mode"])
  );

  Map<String, dynamic> toJson() => {
        "is_on": this.is_on,
        "mode" : this.mode == null ? null : this.mode.toJson()
      };
}

class Device {
  Device({this.uuid, this.name, this.location, this.state, this.supported_modes});

  String uuid;
  String name;
  String location;
  DeviceState state;
  List<int> supported_modes;

  factory Device.fromJson(Map<String, dynamic> json) => Device(
      uuid: json["uuid"],
      name: json["name"],
      location: json["location"],
      state: json["state"] == null ? null : DeviceState.fromJson(json["state"]),
      supported_modes: json["supported_modes"] == null
          ? []
          : json["supported_modes"].cast<int>());

  Map<String, dynamic> toJson() => {
        "uuid": uuid,
        "name": name,
        "location": location,
        "state" : state == null ? null : state.toJson(),
        "supported_modes": supported_modes
      };
}
