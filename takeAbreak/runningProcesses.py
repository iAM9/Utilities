"""
This small stub executes a command to get list of top 5
programs currently running with the longest time .

"""

import os
import sys
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(process)d-%(levelname)s-%(message)s')

try:
    if sys.platform.startswith("win"):
        logging.info("Windows Operating System found..")
        powershellProcess = subprocess.Popen(["powershell", "Get-Process | select starttime,ProcessName,CPU,PM | Sort "
                                                            "starttime -Desc"], stdout=subprocess.PIPE)
        result = powershellProcess.communicate()[0]
        print(result)
    elif sys.platform.startswith("lin"):
        logging.info("Linux Operating System found..")
        command = "ps -o pid=,user=,vsz=,command=,%cpu=,%mem,time -e | sort -nrk 3,3 | head -n 7"
        result = os.system(command)
        print(10/0)
except Exception as exception:
    logging.error("Error ! " , exc_info=True)

