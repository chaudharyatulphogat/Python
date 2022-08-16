device = {'1': 'R1', '2': 'R2', '3': 'R3', '4': 'R4'}
"""
try: 
    device['1']
except:
    print('Device deosn\'t exist')
"""

#We should always define key error in exception. it should not be default.
"""
try: 
    device['5']
except KeyError:
    print('Device deosn\'t exist')
"""

"""
x=1
y=0
try: 
    z=x/y
except ZeroDivisionError as e: 
    print(e)
"""
"""
import sys
import netmiko
from netmiko import NetmikoAuthenticationException as Authfail

try: 
    conn=netmiko.ConnectHandler (
        '10.254.0.1', username='cisco', 
        password='cisco', device_type='cisco_ios'
        )
except Authfail as e: 
    output = e
    sys.exit()

else:
    output=conn.send_command('show running-config')
finally: 
    print(output)
"""


#Sometimes we need to make our own exceptions: 

import requests

ip = 'https://python.org/'
dn = 'about/'
auth=('cisco', 'cisco')
dash = '- *80'

try: 
    response = requests.get(ip+dn) 
    # For network device response = requests.get(ip+dn, auth headers=headers, verify=False
    response.raise_for_status()
#Above will raise HTTP Exception if code is not 200
#Below will catch that exception. 
except requests.HTTPError as e:
    filename='errors.log'
    data = e
else: 
    filename='success.log'
    data = response.content 
finally: 
    with open('filename', 'a') as f: 
        print(data, dash, sep='\n', file=f)













