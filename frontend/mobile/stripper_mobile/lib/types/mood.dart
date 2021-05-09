import 'package:stripper_mobile/types/data.dart';
import 'package:stripper_mobile/types/mood_manipulator.dart';

class Mood {
    Mood({
        this.uuid,
        this.name,
        this.manipulators,
    });

    String uuid;
    String name;
    List<MoodManipulator> manipulators;

    factory Mood.fromJson(Map<String, dynamic> json) => Mood(
        uuid: json["uuid"],
        name: json["name"],
        manipulators: List<MoodManipulator>.from(json["manipulators"].map((x) => MoodManipulator.fromJson(x))),
    );

    Map<String, dynamic> toJson() => {
        "uuid": uuid,
        "name": name,
        "manipulators": List<dynamic>.from(manipulators.map((x) => x)),
    };
}
