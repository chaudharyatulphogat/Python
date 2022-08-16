import json
import pprint 
with open('sample2.json', 'r') as f:
    ip = json.load(f)
    pprint.pprint(ip)