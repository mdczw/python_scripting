#!/usr/bin/env python3

"""script gets system information like distro info, memory(total, used, free),
CPU info (model, core numbers, speed), current user, system load average, and IP address.
-d for distro -m for memory, -c for CPU, -u for user info,
-l for load average, -i for IP address."""

import os
import platform
import argparse
import psutil

def distro_info():
    """Returns distribution information"""
    return platform.system()


def memory_info():
    """Returns memory(total, used, free) information"""
    memory = psutil.virtual_memory()
    return [memory.total, memory.used, memory.available]


def cpu_info():
    """Returns CPU(model, core numbers, speed) information"""
    cpu = [platform.processor(), psutil.cpu_count(), psutil.cpu_freq().current]
    return cpu


def current_user():
    """Returns current user name"""
    return os.getlogin()


def load_average():
    """Returns system load average"""
    load1, load5, load15 = os.getloadavg()
    return [load1, load5, load15]


def ip_address():
    """Returns IP address"""
    return os.popen("ipconfig getifaddr en0").read().strip()

def argument_parser():
    """Parses the command line parameters"""
    parser = argparse.ArgumentParser(description="Get system information")

    parser.add_argument("-d", action="store_true", help="Get distro information")
    parser.add_argument("-m", action="store_true", help="Get memory information")
    parser.add_argument("-c", action="store_true", help="Get CPU information")
    parser.add_argument("-u", action="store_true", help="Get current user information")
    parser.add_argument("-l", action="store_true", help="Get system load average")
    parser.add_argument("-i", action="store_true", help="Get IP address")

    return parser.parse_args()


if __name__ == "__main__":

    args = argument_parser()

    if args.d:
        print(f"Distro: {distro_info()}")
    if args.m:
        print(
            f"""Memory:
            Total: {memory_info()[0] / (1024 ** 3):.2f} Gb, 
            Used: {memory_info()[1] / (1024 ** 3):.2f} Gb, 
            Free: {memory_info()[2] / (1024 ** 3):.2f} Gb"""
        )
    if args.c:
        print(
            f"""CPU:
            Model: {cpu_info()[0]}, 
            Core numbers: {cpu_info()[1]}, 
            Speed: {cpu_info()[2]:.2f} MHz"""
        )
    if args.u:
        print(f"Current user: {current_user()}")
    if args.l:
        print(
            f"""System load average:
            Load average over the last 1 minute: {load_average()[0]:.4f},
            Load average over the last 5 minute: {load_average()[1]:.4f},
            Load average over the last 15 minute: {load_average()[2]:.4f}"""
        )
    if args.i:
        print(f"IP address: {ip_address()}")
