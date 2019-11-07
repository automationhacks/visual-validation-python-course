import subprocess
from subprocess import Popen


def execute_cmd(cmd):
    handle = Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                   shell=True)
    stdout, stderr = handle.communicate()
    return stdout, stderr
