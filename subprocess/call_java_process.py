import subprocess
from typing import List


def jarWrapper(cmd_args: List[str]):
    process = subprocess.call(cmd_args)
    print(process)


cmd = ['java', '-jar', '/Users/jlara/Documents/zemoga_projects/CAP/cap-2681/cap-2681/py4j/javagatewayapp/target'
                       '/JavaGatewayApp-1.0-SNAPSHOT-jar-with-dependencies.jar']
jarWrapper(cmd_args=cmd)
