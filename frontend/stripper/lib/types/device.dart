import 'package:flutter/material.dart';
import 'package:stripper/types/ModeDefinition.dart';

class DeviceState {
  bool? isOn;
  Mode? mode;

  DeviceState({this.isOn, this.mode});

  factory DeviceState.fromJson(Map<String, dynamic> json) => DeviceState(
      isOn: json["is_on"],
      mode: json["c_mode"] == null ? null : Mode.fromJson(json["c_mode"]));

  Map<String, dynamic> toJson() =>
      {"is_on": this.isOn, "mode": this.mode == null ? null : this.mode};
}

class Device {
  Device(
      {this.uuid, this.name, this.location, this.state, this.supportedModes});

  String? uuid;
  String? name;
  String? location;
  DeviceState? state;
  List<int>? supportedModes;

  factory Device.fromJson(Map<String, dynamic> json) => Device(
      uuid: json["uuid"],
      name: json["name"],
      location: json["location"],
      state: json["state"] == null ? null : DeviceState.fromJson(json["state"]),
      supportedModes: json["supported_modes"] == null
          ? []
          : json["supported_modes"].cast<int>());

  Map<String, dynamic> toJson() => {
        "uuid": uuid,
        "name": name,
        "location": location,
        "state": state?.toJson() ?? null,
        "supported_modes": supportedModes
      };
}
