import getpass
import sys
import telnetlib
import time

HOST = "10.201.161.146"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()
Image_name = "cat4500-entservicesk9-mz.150-2.SG7.bin"
tn = telnetlib.Telnet(HOST)

print (tn)
print Image_name

print ("test1") 



tn.read_until("Username: ")
tn.write(user + "\n")

print ("test2")

if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")


print ("Capturing and printing pre-upgrade logs")

# Below syntax is to start upgrade

tn.write("conf t\n")

tn.write("boot system flash bootflash:")
tn.write(Image_name)
tn.write("\n")

tn.write("exit\n")
tn.write("exit\n")



print tn.read_all()

tn = telnetlib.Telnet(HOST)
tn.write("show bootvar\n")
tn.write("exit\n")

print tn.read_all()
