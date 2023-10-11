#!/usr/bin/env python3

import sys
import psutil 
import os
import platform
import socket
import argparse


def distro_info():
    return platform.system()

def memory_info():
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "used": memory.used,
        "free": memory.available,
    }

def cpu_info():
    cpu_info = {}
    cpu_info["model"] = platform.processor()
    cpu_info["core_count"] = psutil.cpu_count(logical=False)
    cpu_info["speed"] = f"{psutil.cpu_freq().current:.2f} MHz"
    return cpu_info

def current_user():
    return os.getlogin()

def load_average():
    load1, load5, load15 = os.getloadavg()
    return {
        "Load average over the last 1 minute": load1,
        "Load average over the last 5 minute": load5,
        "Load average over the last 10 minute": load10
    }

def ip_address():
    return os.popen('ipconfig getifaddr en0').read()



'''
for argument in sys.argv[1:]:
    if argument == "-d":
        print("Distro info:")
        print(platform.system())
        print()

    elif argument == "-m":
        print("Memory info:")
        print("total: {0} bytes, free: {1} bytes, used: {2} bytes".format(psutil.virtual_memory().total, psutil.virtual_memory().available, psutil.virtual_memory().used))
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

'''
   