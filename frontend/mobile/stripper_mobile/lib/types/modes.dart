import 'package:flutter/material.dart';

class Mode {
  int mode_id;
  Mode(this.mode_id);

  factory Mode.fromJson(Map<String, dynamic> json) {
    print("MODE: " + json.toString());
    if (json == null) return null;
    switch (json["mode_id"]) {
      case 0:
        return ModeOff.fromJson(json);
      case 1:
        return ModeSolidColor.fromJson(json);
      case 2:
        return ModeSingleColorPulse.fromJson(json);
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

class ModeSingleColorPulse extends Mode {
  ModeSingleColorPulse(
      {@required this.hue,
      @required this.saturation,
      @required this.value,
      @required this.brightness,
      @required this.brightness_start,
      @required this.brightness_end,
      @required this.speed})
      : super(2);

  int hue;
  int saturation;
  int value;
  int brightness;
  int brightness_start;
  int brightness_end;
  int speed;

  factory ModeSingleColorPulse.fromJson(Map<String, dynamic> json) =>
      ModeSingleColorPulse(
          hue: json["h"],
          saturation: json["s"],
          value: json["v"],
          brightness: json["brightness"],
          brightness_start: json["brightness_start"],
          brightness_end: json["brightness_end"],
          speed: json["speed"]);

  Map<String, dynamic> toJson() => {
        "mode_id": mode_id,
        "h": hue,
        "s": saturation,
        "v": value,
        "brightness": brightness,
        "brightness_start": brightness_start,
        "brightness_end": brightness_end,
        "speed": speed
      };
}
