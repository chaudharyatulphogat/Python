
def func1():
    print(f'__name in function1 is {__name__}')

def func2():
    print('I am function2')

print(__name__)

if __name__ == '__main__':
    print('Running both function')
    func1()
    func2()

