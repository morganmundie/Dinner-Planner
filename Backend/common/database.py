import json
from bson import json_util

def convertBsonToJson(data):
    return json.loads(json_util.dumps(data))