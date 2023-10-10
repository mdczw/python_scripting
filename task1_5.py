#!/usr/bin/env python3

import sys
import psutil 
import os
import platform
import socket

for argument in sys.argv[1:]:
    if argument == "-d":
        print("Distro info:")
        print(platform.system())
        print()

    elif argument == "-m":
        print("Memory info:")
        print("total: {0} bytes, free: {1} bytes, used: {2} bytes".format(psutil.virtual_memory(). total, psutil.virtual_memory().available, psutil.virtual_memory().used))
        print()

    elif argument == "-c":
        print("CPU info:")
        cpu_model = os.system('sysctl -a | grep machdep.cpu.brand_string')
        print("Core Numbers: {0}, Current Frequency: {1}Mhz".format(psutil.cpu_count(), psutil.cpu_freq().current))
        print()

    elif argument == "-u":
        print("Current user:")
        print(os.getlogin())
        print()

    elif argument == "-l":
        load1, load5, load15 = os.getloadavg()
        print("Load average:")
        print("Load average over the last 1 minute:", load1)
        print("Load average over the last 5 minute:", load5)
        print("Load average over the last 15 minute:", load15)
        print()

    elif argument == "-i":
        print("IP address:")
        print(os.popen('ipconfig getifaddr en0').read())

    else:
        print("Invalid parameter: " + str(argument))
        print()
   