# -*- coding: utf-8 -*

import subprocess
import shlex

def run_command(command):
    #process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE,shell=True)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.strip()
    rc = process.poll()
    return rc


cmd = 'vmstat 1'
run_command(cmd)