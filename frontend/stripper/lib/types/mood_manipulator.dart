class MoodManipulator {
  String? stripUuid;
  Map<String, String>? mode;
  MoodManipulator({
    this.stripUuid,
    this.mode,
  });
  factory MoodManipulator.fromJson(Map<String, dynamic> json) =>
      MoodManipulator(
        stripUuid: json["uuid"],
        mode: json["mode"],
      );

  Map<String, dynamic> toJson() => {
        "uuid": stripUuid,
        "mode": mode,
      };
}
