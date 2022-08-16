import re 
pattern = 'net[1-4]'
interface = 'This interface is GigabitEthernet3 pwnet1 sdnet2 powenet1'
result = re.split(pattern, interface)
print(result)

