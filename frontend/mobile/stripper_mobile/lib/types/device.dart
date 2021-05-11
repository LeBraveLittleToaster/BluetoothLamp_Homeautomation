class Device {
  Device({this.uuid, this.name, this.location, this.supported_modes});

  String uuid;
  String name;
  String location;
  List<int> supported_modes;

  factory Device.fromJson(Map<String, dynamic> json) => Device(
      uuid: json["uuid"],
      name: json["name"],
      location: json["location"],
      supported_modes: json["supported_modes"] == null
          ? []
          : json["supported_modes"].cast<int>());

  Map<String, dynamic> toJson() => {
        "uuid": uuid,
        "name": name,
        "location": location,
        "supported_modes": supported_modes
      };
}
