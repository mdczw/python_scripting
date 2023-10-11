#!/usr/bin/env python3

import psutil 
import os
import platform
import argparse


def distro_info():
    return platform.system()

def memory_info():
    memory = psutil.virtual_memory()
    return [memory.total, memory.used, memory.available]
        
def cpu_info():
    cpu_info = [platform.processor(), psutil.cpu_count(), psutil.cpu_freq().current]
    return cpu_info

def current_user():
    return os.getlogin()

def load_average():
    load1, load5, load15 = os.getloadavg()
    return [load1, load5, load15]

def ip_address():
    return os.popen('ipconfig getifaddr en0').read().strip()

parser = argparse.ArgumentParser(description='Get system information')

parser.add_argument('-d', action='store_true', help='Get distro information')
parser.add_argument('-m', action='store_true', help='Get memory information')
parser.add_argument('-c', action='store_true', help='Get CPU information')
parser.add_argument('-u', action='store_true', help='Get current user information')
parser.add_argument('-l', action='store_true', help='Get system load average')
parser.add_argument('-i', action='store_true', help='Get IP address')

args = parser.parse_args()

if args.d:
    print(f"Distro: {distro_info()}")
if args.m:
    print(f"Memory:\nTotal: {memory_info()[0] / (1024 ** 3):.2f} Gb, Used: {memory_info()[1] / (1024 ** 3):.2f} Gb, Free: {memory_info()[2] / (1024 ** 3):.2f} Gb")
if args.c:
    print(f"CPU:\nModel: {cpu_info()[0]}, Core numbers: {cpu_info()[1]}, Speed: {cpu_info()[2]:.2f} MHz")
if args.u:
    print(f"Current user: {current_user()}")
if args.l:
    print(f"System load average:\nLoad average over the last 1 minute: {load_average()[0]:.4f},\nLoad average over the last 5 minute: {load_average()[1]:.4f},\nLoad average over the last 15 minute: {load_average()[2]:.4f}")
if args.i:
    print(f"IP address: {ip_address()}")
