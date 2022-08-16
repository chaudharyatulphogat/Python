#devices = {"device": "router1", "model": 3800, "os": "IOS-XE" }

#devices = ["Router", "Router1", "Router2", "Router3", "Router4"]

import Testmain
import Regexpractice


def func3():
    print('I am function3')

print(f'Value of __name__ before main is {__name__}')

def main():
    print(f'Value of __name__ in main is {__name__}')
    Testmain.func1()
    Testmain.func2()
    func3()

main()
