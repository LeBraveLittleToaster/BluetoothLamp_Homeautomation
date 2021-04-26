import getopt
import sys
from typing import List

from flask import Flask
from flask_cors import CORS

from de.pschiessle.stripper.distributor.core import HttpHandler
from de.pschiessle.stripper.shared.config.Config import NodeConfig
from de.pschiessle.stripper.shared.dbcon.MongoDbCon import MongoDbCon


def usage():
    print("-c or -config: file path to config\n-h -help: shows available commands")


try:
    opts, args = getopt.getopt(sys.argv[1:], 'c:h', ['config=', 'help'])
except getopt.GetoptError:
    usage()
    sys.exit("wrong arguments")

node_config = None

for opt, arg in opts:
    if opt in ('-c', '--config'):
        node_config = NodeConfig(arg)
    elif opt in ('-h', '--help'):
        usage()
        sys.exit(2)
    else:
        usage()
        sys.exit(2)

if node_config is not None:
    missing: List[str] = node_config.check_config()
    if len(missing) > 0:
        print("Missing config entries: " + str(missing))
        sys.exit(2)
else:
    print("No config found!")
    sys.exit(2)

mongo_con = MongoDbCon(node_config)

app: Flask = Flask("__main__")
cors: CORS = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'


@app.route("/nodes/ping/all")
def ping_all():
    return HttpHandler.handle_node_ping_all_get(mongo_con).get_as_json_str()


app.run(host='0.0.0.0', port=node_config.node_port, debug=False)
