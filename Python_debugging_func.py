#Python debugging function break or sys.exit()
"""
import subprocess
import sys
count=0
while True: 
    if count > 2:
        sys.exit('ping to 127.0.0.1 failed')
        #or print('ping to 127.0.0.1 failed')
        #break
    p = subprocess.Popen('ping 127.0.0.2 -c 1', shell=True)
    p.wait()
    if p.poll() == 0: 
        print('Ping to 127.0.0.1 successful')
        break
    else:
        pass
    count+=1
"""

#Logging: 
"""
import Logging
import netmiko 


logging.basicConfig(
    file='mylog.txt',
    format = f"%(asctime)s \n%(levelname)s: %(message)s \n{'-'*80}",
    datefmt='%x %X %Z',
    level=logging.INFO
)
"""

import netmiko

ip_list = ['10.254.0.1', '10.254.0.2', '10.254.0.3', '10.254.0.4']
for ip in ip_list: 
    try: 
        conn = netmiko.ConnectHandler(ip, username='cisco', 
            password='cisco', device_type='cisco_ios'
            )
    except netmiko.NetmikoTimeoutException:
        log_message= f'{ip} - Timeout Check IP, TCP, PORT etc please'
        logging.error(log_message)
    else: 
        logging.info('Connection established to %s', ip)
        print(conn.send_command('show run'))



    