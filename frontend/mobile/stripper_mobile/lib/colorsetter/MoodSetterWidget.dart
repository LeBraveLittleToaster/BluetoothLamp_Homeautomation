import 'package:flutter/material.dart';
import 'package:flutter_slidable/flutter_slidable.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:stripper_mobile/net/requester.dart';
import 'package:stripper_mobile/types/mood.dart';

class MoodSetterWidget extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _MoodSetterState();
}

class _MoodSetterState extends State<MoodSetterWidget> {
  Future<List<Mood>> moodsF;

  String active_mood_uuid;

  _setMood(String mood_uuid) {
    setState(() {
      active_mood_uuid = mood_uuid;
    });
    Requester.setMood(mood_uuid);
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<Mood>>(
        future: Requester.getMoodList(),
        builder: (context, snapshot) {
          return snapshot.hasData
              ? ListView.builder(
                  itemCount: snapshot.data == null ? 0 : snapshot.data.length,
                  itemBuilder: (context, index) {
                    return Slidable(
                        actionPane: SlidableStrechActionPane(),
                        actionExtentRatio: 0.25,
                        secondaryActions: [
                          IconSlideAction(
                            caption: "Delete",
                            color: Colors.red,
                            icon: Icons.more_horiz,
                            onTap: () {
                              Requester.deleteMood(snapshot.data[index].uuid)
                                  .then((value) => setState(() {}));
                            },
                          )
                        ],
                        child: ListTile(
                          title: Text(snapshot.data[index].name),
                          trailing: IconButton(
                            icon: Icon(
                              Icons.line_weight,
                            ),
                            onPressed: () =>
                                _setMood(snapshot.data[index].uuid),
                          ),
                        ));
                  })
              : Center(
                  child: SpinKitCubeGrid(
                    color: Colors.amber,
                  ),
                );
        });
  }
}
