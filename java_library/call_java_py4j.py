import numpy as np
from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
helloJava = gateway.entry_point.getMain()

if __name__ == '__main__':
    print('Getting double value from calculation with offset'.center(50, '-'))
    print(helloJava.getTotal(40).getTotal())
    print(helloJava.getTotal(45).getTotal())
    print(helloJava.getTotal(50).getTotal())

    print('Getting double value from calculation without offset'.center(50, '-'))
    print(helloJava.getTotal().getTotal())

    print('Printing new string message'.center(50, '-'))
    print(helloJava.getMessage())
    print(helloJava.getMessage())
    print(helloJava.getMessage())

    print('Executing threading method'.center(50, '-'))
    helloJava.execute_threading()

    print('Printing new string message'.center(50, '-'))
    print(helloJava.getMessage())

    print('Executing threading operation'.center(50, '-'))
    total_value = helloJava.execute_threading_forkjoin()
    print(total_value)

    print('Getting a list from Java'.center(50, '-'))
    calculation_list = helloJava.getCalculationList(50)
    print(len(calculation_list))
    print(f'first element from list {calculation_list[0]}')
    print(f'last element from list {calculation_list[-1]}')

    a = np.array(calculation_list)
    b = np.arange(len(calculation_list))
    print(f'Array calculated from Java: {a}')
    print(f'Array created by Numpy {b}')

    c = a - b
    print(f'Array Operation with Numpy {c}')




