import sys
import argparse
#arg_list[]
#print (f'Number of arguement: {len(sys.argv)}')
#print (f'List of argument: {str(sys.argv)}')
#arg_list = sys.agrv
#print (arg_list)

text = "This python takes input for router information"
parser = argparse.ArgumentParser(description=text)
parser.add_argument("-R", "--router", help="Enter router name")
parser.add_argument("-IP", help="Enter IP address")

router = parser.parse_args()
print(f'Router name is {router.router} IP is {router.IP}')


