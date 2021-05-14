import 'package:flutter/material.dart';

class Mode {
  int mode_id;
  Mode(this.mode_id);

  factory Mode.fromJson(Map<String, dynamic> json) {
    if (json == null) return null;
    switch (json["mode_id"]) {
      case 0:
        return ModeOff.fromJson(json);
      case 1:
        return ModeSolidColor.fromJson(json);
      default:
        return ModeOff();
    }
  }

  Map<String, dynamic> toJson() => {"mode_id": this.mode_id};
}

class ModeOff extends Mode {
  ModeOff() : super(0);
  factory ModeOff.fromJson(Map<String, dynamic> json) => ModeOff();

  Map<String, dynamic> toJson() => super.toJson();
}

class ModeSolidColor extends Mode {
  ModeSolidColor(
      {@required this.hue,
      @required this.saturation,
      @required this.value,
      @required this.brightness})
      : super(1);

  int hue;
  int saturation;
  int value;
  int brightness;

  factory ModeSolidColor.fromJson(Map<String, dynamic> json) => ModeSolidColor(
      hue: json["h"],
      saturation: json["s"],
      value: json["v"],
      brightness: json["brightness"]);

  Map<String, dynamic> toJson() => {
        "mode_id": mode_id,
        "h": hue,
        "s": saturation,
        "v": value,
        "brightness": brightness
      };
}
