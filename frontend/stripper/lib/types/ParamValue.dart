import 'package:stripper/modes/ModeDefinition.dart';

class ParamValue {
  final ParamType? paramType;
  final int? paramLength;
  dynamic value;

  ParamValue({required this.paramType, required this.paramLength, this.value});

  factory ParamValue.fromJson(Map<String, dynamic> json) {
    return ParamValue(
        paramType: paramTypeFromString(json["param_type"]),
        paramLength: json["param_length"],
        value: json["value"]);
  }

  Map<String, dynamic> toJson() => {
        "param_type": this
            .paramType
            ?.toString()
            .substring(this.paramType.toString().indexOf(".") + 1),
        "param_length": this.paramLength,
        "value": this.value
      };
  @override
  String toString() {
    return "paramType: " +
        (paramType?.toString() ?? "none") +
        "colorParams: " +
        (paramLength?.toString() ?? "none") +
        "modeParams: " +
        (value?.toString() ?? "none");
  }
}
