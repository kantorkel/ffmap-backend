#!/usr/bin/env python3
import subprocess
import json

from collections import MutableMapping

def rec_merge(d1, d2):
    '''
    Update two dicts of dicts recursively, 
    if either mapping has leaves that are non-dicts, 
    the second's leaf overwrites the first's.
    '''
    for k, v in d1.items(): # in Python 2, use .iteritems()!
        if k in d2:
            # this next check is the only difference!
            if all(isinstance(e, MutableMapping) for e in (v, d2[k])):
                d2[k] = rec_merge(v, d2[k])
            # we could further check types and merge as appropriate here.
    d3 = d1.copy()
    d3.update(d2)
    return d3


class alfred_merge:
  def __init__(self,request_data_type_1 = 158, request_data_type_2 = 159):
    self.request_data_type_1 = request_data_type_1
    self.request_data_type_2 = request_data_type_2

  def aliases(self):
    output = subprocess.check_output(["/usr/local/bin/alfred-json","-z", "-r",str(self.request_data_type_1),"-f","json"])
    alfred_data_1 = json.loads(output.decode("utf-8"))
    output = subprocess.check_output(["/usr/local/bin/alfred-json","-z", "-r",str(self.request_data_type_2),"-f","json"])
    alfred_data_2 = json.loads(output.decode("utf-8"))
    
    return json.dumps(rec_merge(alfred_data_1, alfred_data_2))


if __name__ == "__main__":
  ad = alfred_merge()
  al = ad.aliases()
  print(al)

