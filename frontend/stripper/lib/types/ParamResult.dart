import 'package:stripper/modes/ModeDefinition.dart';

class ParamResult {
  final ParamType paramType;
  final int paramLength;
  dynamic value;

  ParamResult({required this.paramType, required this.paramLength, this.value});
}
