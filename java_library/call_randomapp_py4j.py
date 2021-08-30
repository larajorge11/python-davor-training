from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
securityIdPercentageApp = gateway.entry_point.getSecurityIdCalculationObject()

if __name__ == '__main__':

    val = securityIdPercentageApp.calculatePercentageSecurityIDs(1, 1)
    print('finish')