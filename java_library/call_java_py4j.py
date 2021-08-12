from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
addition_app = gateway.entry_point
addition_app.execute_threading()
