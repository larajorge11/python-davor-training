import numpy as np
from py4j.java_gateway import JavaGateway, GatewayParameters

gateway = JavaGateway(gateway_parameters=GatewayParameters(auto_convert=True))
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
    calculation_list = helloJava.getCalculationList_2(50)
    print(len(calculation_list))
    print(f'first element from list {calculation_list[0]}')
    print(f'last element from list {calculation_list[-1]}')

    val = helloJava.getTestData(2, 2)
    print('finish')




