import getopt
import sys

from flask import Flask
from flask_cors import CORS

from de.pschiessle.services.distributer import HttpHandler
from de.pschiessle.services.distributer.Config import Config
from de.pschiessle.services.distributer.MongoDbCon import MongoDbCon


def usage():
    print("Wrong arguments")


try:
    opts, args = getopt.getopt(sys.argv[1:], 'c:h', ['config=', 'help'])
except getopt.GetoptError:
    usage()
    sys.exit("wrong arguments")

for opt, arg in opts:
    if opt in ('-c', '--config'):
        config = Config(arg)
        config.check_config()
    elif opt in ('-h', '--help'):
        usage()
        sys.exit(2)
    else:
        usage()
        sys.exit(2)

mongo_con = MongoDbCon(config)

app: Flask = Flask("__main__")
cors: CORS = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'


@app.route("/nodes/ping/all")
def ping_all():
    return HttpHandler.handle_node_ping_all_get(mongo_con)


app.run(host='0.0.0.0', port=4321, debug=False)
