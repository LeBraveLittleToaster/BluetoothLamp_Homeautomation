class Device {
    Device({
        this.uuid,
        this.name,
        this.location,
    });

    String uuid;
    String name;
    String location;

    factory Device.fromJson(Map<String, dynamic> json) => Device(
        uuid: json["uuid"],
        name: json["name"],
        location: json["location"],
    );

    Map<String, dynamic> toJson() => {
        "uuid": uuid,
        "name": name,
        "location": location,
    };
}