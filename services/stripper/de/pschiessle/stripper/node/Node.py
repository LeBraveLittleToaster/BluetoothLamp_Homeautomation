import getopt
import sys
from typing import Optional

from flask import Flask
from flask_cors import CORS

from de.pschiessle.stripper.node.core import HttpHandler
from de.pschiessle.stripper.shared.config.Config import NodeConfig, DeviceConfig
from de.pschiessle.stripper.shared.dbcon.MongoDbCon import MongoDbCon


def usage():
    print("Wrong arguments")


try:
    opts, args = getopt.getopt(sys.argv[1:], 'c:d:h', ['config=', 'devices=', 'help'])
except getopt.GetoptError:
    usage()
    sys.exit("wrong arguments")

node_config: Optional[NodeConfig] = None
device_config: Optional[DeviceConfig] = None

for opt, arg in opts:
    if opt in ('-c', '--config'):
        node_config = NodeConfig(arg)
    elif opt in ('-d', '--devices'):
        device_config = DeviceConfig(arg)
    elif opt in ('-h', '--help'):
        usage()
        sys.exit(2)
    else:
        usage()
        sys.exit(2)

if node_config is None or device_config is None:
    print("Node or device config is missing")
    sys.exit(2)
else:
    missing_node_conf = node_config.check_config()
    missing_device_conf = device_config.check_config()
    if len(missing_device_conf) > 0 or len(missing_node_conf) > 0:
        print("Missing entries in node config: " + str(missing_node_conf))
        print("Missing entries in device config: " + str(missing_device_conf))
        sys.exit(2)

mongo_con = MongoDbCon(node_config)

app: Flask = Flask("__main__")
cors: CORS = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'


@app.route("/ping")
def ping():
    return HttpHandler.handle_ping_get().get_as_json_str()


if mongo_con.do_register_node():
    print("Node online...")
    if mongo_con.do_register_devices(device_config):
        print("Devices registered...")
    else:
        print("Failed to register devices...")
else:
    print("Failed to register node...")
    sys.exit(2)

app.run(host='0.0.0.0', port=1234, debug=False)
