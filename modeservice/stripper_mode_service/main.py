from flask import Flask, request, abort
from flask_cors import CORS

from stripper_mode_service.db.mongo_connector import MongoConnector, MongoDbConfig

db_con = MongoConnector(MongoDbConfig.get_default_config())

app = Flask(__name__)
CORS(app)


app.run("0.0.0.0", 1212)
