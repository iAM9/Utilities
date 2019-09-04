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
        POWERSHELL_PROCESS = subprocess.Popen(["powershell", "Get-Process | select starttime,ProcessName,CPU,PM | Sort starttime -Desc"], stdout=subprocess.PIPE)
        RESULT = POWERSHELL_PROCESS.communicate()[0]
        print(RESULT)

    elif sys.platform.startswith("lin"):
        logging.info("Linux Operating System found..")
        COMMAND = "ps -o pid=,user=,vsz=,command=,%cpu=,%mem,time -e | sort -nrk 3,3 | head -n 7"
        RESULT = os.system(COMMAND)

except Exception as exception:
    logging.error("Error!", exc_info=True)
