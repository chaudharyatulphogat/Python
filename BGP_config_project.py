import netmiko
from getpass import getpass
import logging
import os
import time
import csv
import pandas as pd

#Details to login into device. 
username = input("Enter username:")
print ("check for password")
password = getpass("Password:")
device_ip = str(input("Enter the device IP: "))

# BGP variables
self_ip = str(input("Enter the BGP self IP: "))
peer_ip = str(input("Enter the BGP peer IP: "))
self_AS = int(input("Enter self AS number: "))
remote_AS = int (input("Enter remote AS number:"))

device_select=str(input('Enter IOS or XE:'))


print (device_ip)
print (peer_ip)
print (self_AS)
print (remote_AS)

class ssh_connection:
    
    def __init__(self, ip, username=None, password=None):
        self.conn_data = {
            'ip' : ip,
            'username': username,
            'password': password,
            'device_type': 'cisco_ios'
        }

    def login(self):    
        try: 
            self.conn = netmiko.ConnectHandler(**self.conn_data)
        except netmiko.NetmikoTimeoutException:
            log_message=f'{device_ip} Check IP, TCP PORT, Connection'
            logging.error(log_message)
        except netmiko.NetmikoAuthenticationException:
            log_message=f'{device_ip} Incorrect username or password.'
            logging.error(log_message)
        else: 
            logging.info('Connection established with %s', device_ip)


class ios_bgp_config(ssh_connection):

    def config_ios_bgp(self):
        self.conn.send_command('config t')
        self.conn.send_command('interface lo0')

ios_router1 = ios_bgp_config(device_ip, username = username, password = password)



if __name__ == '__main__':
    if device_select == "IOS":
        ios_router1.login()
        ios_router1.config_ios_bgp()
    elif device_select == "XE":
        print('code for XE')
    else:
        print ("Unsupported device type. Please choose IOS or IOS-XE")









