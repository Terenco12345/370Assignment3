# A process to use increasing amounts of memory.

import os
import subprocess # run only added in Python 3.5
import time

def show_info(pid):
    # print('\nfree')
    # print('====')
    # subprocess.run(['free'])

    print('\nvmstat -a')
    print('=========')
    subprocess.run(['vmstat', '-a'])

    # print('\n/proc/meminfo')
    # print('=============')
    # subprocess.run(['cat /proc/meminfo | egrep "MemFree|MemAvailable"'], shell=True)

    # print('\nOOM score')
    # print('=========')
    # subprocess.run(['cat', '/proc/{}/oom_score'.format(pid)])

    # print('\n/proc/pid/maps')
    # print('==============')
    # subprocess.run(['cat', '/proc/{}/maps'.format(pid)])

    # print('\n/pro/pid/map_files')
    # print('==================')
    # subprocess.run(['ls', '-l', '/proc/{}/map_files'.format(pid)])

big_list = []
LIST_INCREMENT=10000000
up_to = 0
my_pid = os.getpid()
show_info(my_pid)
for i in range(20):
    big_list += list(range(up_to, up_to + LIST_INCREMENT))
    show_info(my_pid)
    print("subprocess completed")
    up_to += LIST_INCREMENT
print("The End")
