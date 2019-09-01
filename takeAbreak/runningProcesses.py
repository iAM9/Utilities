"""
This small stub executes a command to get list of top 5
programs currently running with the longest time .

"""

import os

files = "ps -o pid=,user=,vsz=,command=,%cpu=,%mem,time -e | sort -nrk 3,3 | head -n 7"
programs = os.system(files)
print(programs)
