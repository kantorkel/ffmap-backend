import json


def validate_nodeinfos(nodeinfos):
    result = []

    for nodeinfo in nodeinfos:
        nodeinfo = remove_garbage(nodeinfo)
        if validate_nodeinfo(nodeinfo):
            result.append(nodeinfo)

    return result


def remove_garbage(nodeinfo):
    garbage_keys = []
    for k, v in nodeinfo.items():
      if k.startswith('function:'):
        garbage_keys.append(k)
      elif isinstance(v, dict):
        remove_garbage(v)
    for k in garbage_keys:
      del nodeinfo[k]
    return nodeinfo


def validate_nodeinfo(nodeinfo):
    if 'location' in nodeinfo:
        if 'latitude' not in nodeinfo['location'] or 'longitude' not in nodeinfo['location']:
            return False

    return True
