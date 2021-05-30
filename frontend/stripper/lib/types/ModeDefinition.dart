import 'package:stripper/types/ParamValue.dart';
import 'package:tuple/tuple.dart';

class Mode {
  final int? modeId;
  final List<Tuple2<String, ParamValue>>? colorValues;
  final List<Tuple2<String, ParamValue>>? modeValues;

  Mode({this.modeId, this.colorValues, this.modeValues});

  factory Mode.fromJson(Map<String, dynamic> json) {
    Map<String, dynamic>? colorParams = json["color_params"];
    Map<String, dynamic>? modeParams = json["mode_params"];
    return Mode(
        modeId: json["mode_id"],
        colorValues: colorParams?.entries
                .map((e) => Tuple2<String, ParamValue>.fromList(
                    [e.key, ParamValue.fromJson(e.value)]))
                .toList() ??
            [],
        modeValues: modeParams?.entries
                .map((e) => Tuple2<String, ParamValue>.fromList(
                    [e.key, ParamValue.fromJson(e.value)]))
                .toList() ??
            []);
  }

  @override
  String toString() {
    return "ModeId: " +
        (modeId?.toString() ?? "none") +
        "colorParams: {\n" +
        (colorValues?.toString() ?? "none") +
        "\n}," +
        "modeParams: {\n" +
        (modeValues?.toString() ?? "none") +
        "\n}";
  }
}

class ModeDefinition {
  final int? modeId;
  final List<ColorParam>? colorParams;
  final List<ModeParam>? modeParams;
  ModeDefinition({this.modeId, this.colorParams, this.modeParams});

  factory ModeDefinition.fromJson(Map<String, dynamic> json) {
    print(json);
    return ModeDefinition(
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
  final int? paramLength;
  final String? jsonKey;
  ModeParam(
      {this.modeParamType,
      this.label,
      this.jsonKey,
      this.paramLength,
      this.paramType});
  factory ModeParam.fromJson(Map<String, dynamic> json) {
    return ModeParam(
        modeParamType: modeParamTypeFromString(json["mode_param_type"]),
        paramType: paramTypeFromString(json["param_type"]),
        paramLength: json["param_length"],
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
        "paramLength: " +
        (paramLength?.toString() ?? "none") +
        "label: " +
        (label?.toString() ?? "none");
  }
}

class ColorParam {
  final ColorParamType? colorParamType;
  final String? label;
  final ParamType? paramType;
  final int? paramLength;
  final String? jsonKey;
  ColorParam(
      {this.colorParamType,
      this.label,
      this.jsonKey,
      this.paramLength,
      this.paramType});
  factory ColorParam.fromJson(Map<String, dynamic> json) {
    return ColorParam(
        colorParamType: colorParamTypeFromString(json["color_param_type"]),
        paramType: paramTypeFromString(json["param_type"]),
        paramLength: json["param_length"],
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
        "paramLength: " +
        (paramLength?.toString() ?? "none") +
        "label: " +
        (label?.toString() ?? "none");
  }
}

//++++++++++++++++++++++++++ENUMS++++++++++++++++++++++++++++++++++++
enum ModeParamType { EMPTY, SINGLE_VALUE, RANGE_VALUE }
enum ColorParamType { EMPTY, HSV_B }
enum ParamType { EMPTY, ARRAY, SINGLE_VALUE }

//+++++++++++++++++++++++++CONVERTER+++++++++++++++++++++++++++++++
ModeParamType modeParamTypeFromString(String value) {
  switch (value) {
    case "SINGLE_VALUE":
      return ModeParamType.SINGLE_VALUE;
    case "RANGE_VALUE":
      return ModeParamType.RANGE_VALUE;
    default:
      return ModeParamType.EMPTY;
  }
}

ColorParamType colorParamTypeFromString(String value) {
  switch (value) {
    case "HSV_B":
      return ColorParamType.HSV_B;
    default:
      return ColorParamType.EMPTY;
  }
}

ParamType paramTypeFromString(String value) {
  switch (value) {
    case "SINGLE_VALUE":
      return ParamType.SINGLE_VALUE;
    case "ARRAY":
      return ParamType.ARRAY;
    default:
      return ParamType.EMPTY;
  }
}
