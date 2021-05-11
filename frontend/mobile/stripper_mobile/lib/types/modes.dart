class Mode {
  int mode_id;
  Mode(this.mode_id);

  factory Mode.fromJson(Map<String, dynamic> json) {
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
  ModeSolidColor({
    this.hue,
    this.saturation,
    this.value,
  }) : super(1);

  int hue;
  int saturation;
  int value;

  factory ModeSolidColor.fromJson(Map<String, dynamic> json) => ModeSolidColor(
        hue: json["hue"],
        saturation: json["saturation"],
        value: json["value"],
      );

  Map<String, dynamic> toJson() => {
        "mode_id": mode_id,
        "hue": hue,
        "saturation": saturation,
        "value": value,
      };
}
