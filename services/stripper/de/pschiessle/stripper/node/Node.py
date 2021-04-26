import getopt
import sys

from flask import Flask
from flask_cors import CORS

from de.pschiessle.stripper.node.core import HttpHandler
from de.pschiessle.stripper.shared.config.Config import Config
from de.pschiessle.stripper.shared.dbcon.MongoDbCon import MongoDbCon


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


@app.route("/ping")
def ping():
    return HttpHandler.handle_ping_get().get_as_json_str()


if mongo_con.do_register_node():
    print("Node online")
else:
    print("Failed to register node...")
    sys.exit(2)

app.run(host='0.0.0.0', port=1234, debug=False)
