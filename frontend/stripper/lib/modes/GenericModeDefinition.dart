class GenericModeDefinition {
  final int? modeId;
  final List<ColorParam>? colorParams;
  final List<ModeParam>? modeParams;
  GenericModeDefinition({this.modeId, this.colorParams, this.modeParams});

  factory GenericModeDefinition.fromJson(Map<String, dynamic> json) {
    print(json);
    return GenericModeDefinition(
        modeId: json["mode_id"] ?? -1,
        colorParams: List<ColorParam>.from(
            json["color_params"]?.map((x) => ColorParam.fromJson(x))),
        modeParams: List<ModeParam>.from(
            json["mode_params"]?.map((x) => ModeParam.fromJson(x)).toList()));
  }
  @override
  String toString() {
    return "ModeId: " +
        (modeId?.toString() ?? "none") +
        "colorParams: {\n" +
        (colorParams?.toString() ?? "none") +
        "\n}," +
        "modeParams: {\n" +
        (modeParams?.toString() ?? "none") +
        "\n}";
  }
}

class ModeParam {
  final ModeParamType? modeParamType;
  final String? label;
  final ParamType? paramType;
  final String? jsonKey;
  ModeParam({this.modeParamType, this.label, this.jsonKey, this.paramType});
  factory ModeParam.fromJson(Map<String, dynamic> json) {
    return ModeParam(
        modeParamType: modeParamTypeFromString(json["mode_param_type"]),
        paramType: paramTypeFromString(json["param_type"]),
        label: json["label"],
        jsonKey: json["json_key"] ?? null);
  }
  @override
  String toString() {
    return "modeParamType: " +
        (modeParamType?.toString() ?? "none") +
        "paramType: " +
        (paramType?.toString() ?? "none") +
        "jsonKey: " +
        (jsonKey?.toString() ?? "none") +
        "label: " +
        (label?.toString() ?? "none");
  }
}

class ColorParam {
  final ColorParamType? colorParamType;
  final String? label;
  final ParamType? paramType;
  final String? jsonKey;
  ColorParam({this.colorParamType, this.label, this.jsonKey, this.paramType});
  factory ColorParam.fromJson(Map<String, dynamic> json) {
    return ColorParam(
        colorParamType: colorParamTypeFromString(json["color_param_type"]),
        paramType: paramTypeFromString(json["param_type"]),
        label: json["label"],
        jsonKey: json["json_key"] ?? null);
  }
  @override
  String toString() {
    return "colorParamType: " +
        (colorParamType?.toString() ?? "none") +
        "paramType: " +
        (paramType?.toString() ?? "none") +
        "jsonKey: " +
        (jsonKey?.toString() ?? "none") +
        "label: " +
        (label?.toString() ?? "none");
  }
}

//++++++++++++++++++++++++++ENUMS++++++++++++++++++++++++++++++++++++
enum ModeParamType { SINGLE_VALUE, RANGE_VALUE }
enum ColorParamType { HSV_B }
enum ParamType { ARRAY, SINGLE_VALUE }

//+++++++++++++++++++++++++CONVERTER+++++++++++++++++++++++++++++++
ModeParamType? modeParamTypeFromString(String value) {
  switch (value) {
    case "SINGLE_VALUE":
      return ModeParamType.SINGLE_VALUE;
    case "RANGE_VALUE":
      return ModeParamType.RANGE_VALUE;
    default:
      return null;
  }
}

ColorParamType? colorParamTypeFromString(String value) {
  switch (value) {
    case "HSV_B":
      return ColorParamType.HSV_B;
    default:
      return null;
  }
}

ParamType? paramTypeFromString(String value) {
  switch (value) {
    case "SINGLE_VALUE":
      return ParamType.SINGLE_VALUE;
    case "ARRAY":
      return ParamType.ARRAY;
    default:
      return null;
  }
}
