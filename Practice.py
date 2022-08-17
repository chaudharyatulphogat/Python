import netmiko 
import sys
import logging

ip_list = ['41.138.51.216']

for ip in ip_list:
    try: 
        conn = netmiko.ConnectHandler(ip, username='ricky', password='F3b_2o12', device_type='cisco_ios')
    except netmiko.NetmikoTimeoutException:
        log_message=f'{ip} Check IP, TCP, PORT, Connection'
        logging.error(log_message)
    else: 
        logging.info('connection established with %s', ip)
        runn_config= conn.send_command('show run')
        filename='runn_config_of'+ str(ip) +'.txt'
        with open(filename, "w") as f:
            f.write(runn_config)


        