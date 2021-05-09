import 'package:stripper_mobile/types/modes.dart';

class MoodManipulator {
    MoodManipulator({
        this.strip_uuid,
        this.mode,
    });

    String strip_uuid;
    Mode mode;

    factory MoodManipulator.fromJson(Map<String, dynamic> json) => MoodManipulator(
        strip_uuid: json["uuid"],
        mode: Mode.fromJson(json["mode"]),
    );

    Map<String, dynamic> toJson() => {
        "uuid": strip_uuid,
        "mode": mode.toJson(),
    };
}

