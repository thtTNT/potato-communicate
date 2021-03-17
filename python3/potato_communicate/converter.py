import json


def toPCO(obj):
    return json.dumps(obj)


def fromPCO(pco):
    return json.loads(pco)
