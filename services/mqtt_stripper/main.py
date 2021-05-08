from typing import List

from flask import Flask
from flask_cors import CORS

from mqtt_stripper.strips.db.modes import ModeOff, ModeSolidColor
from mqtt_stripper.strips.db.mongo_connector import MongoConnector, MongoDbConfig, AlreadyPresentException
from mqtt_stripper.strips.db.mood import MoodManipulator

app = Flask(__name__)
CORS(app)

# with open('../default_config.json') as config_json:
#    config: RunnerConfig = RunnerConfig.from_dict(json.load(config_json))


mongo_con = MongoConnector(MongoDbConfig.get_default_config())
try:
    mongo_con.add_device("uuid1", "name", "loc", "in", "out")
except AlreadyPresentException as e:
    print("Device uuid1 already in database...")

try:
    mongo_con.add_device("uuid2", "name2", "loc2", "in2", "out2")
except AlreadyPresentException as e:
    print("Device uuid2 already in database...")

try:
    manis: List[MoodManipulator] = [MoodManipulator("uuid1", ModeOff()),
                                    MoodManipulator("uuid1", ModeSolidColor(123, 321, 111))]
    mongo_con.add_mood("uuid_mood", "Moodname", manis)
except AlreadyPresentException as e:
    print("Mood uuid_mood already in database...")

print(mongo_con.get_device("uuid1"))
print(mongo_con.get_mood_list())

# app.run("0.0.0.0", 4321)
