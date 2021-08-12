import subprocess
from typing import List


def jarWrapper(cmd_args: List[str]):
    process = subprocess.call(cmd_args)
    print(process)


cmd = ['java', '-jar', 'HelloWorld.jar']
jarWrapper(cmd_args=cmd)
