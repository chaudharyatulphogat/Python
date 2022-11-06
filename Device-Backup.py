import netmiko 
import sys
import logging
import os
import time 
import csv
import pandas as pd

timestr = time.strftime("%Y%m%d-%H%M%S")
print (f'Time is {timestr}')


print('Fetching list of IP from excel file  \n....... ')
devices = pd.read_csv('C:/Users/Administrator/Desktop/Program_logs/Device_list.csv')
ip_list=devices['Device_IPs'].tolist()

print(f'Running config to be collected of IPs: {ip_list} \n........')
#ip_list = ['41.138.51.216','41.138.51.233']

for ip in ip_list:
    try: 
        conn = netmiko.ConnectHandler(ip, username='backup', password='B1l@ckDaug', device_type='cisco_ios')
    except netmiko.NetmikoTimeoutException:
        log_message=f'{ip} Check IP, TCP, PORT, Connection'
        logging.error(log_message)
    else: 
        logging.info('connection established with %s', ip)
#Creating directory to save config file. 
        parent_path = 'C:/Users/Administrator/Desktop/Program_logs'
        directory =  str(ip) + '-' + timestr
        path = os.path.join(parent_path, directory)
        os.makedirs(path,exist_ok=True)
        print("Directory %s is created at %s \n....... " % (directory, parent_path))
#Collecting and saving running configuration. 
        runn_config= conn.send_command('show run')
        filename='runn_config_of'+ str(ip) + '-' + timestr + '.txt'
        with open(path+'/'+filename, "w") as f:
            f.write(runn_config)
        print("Running config file %s has been created" % filename)


        