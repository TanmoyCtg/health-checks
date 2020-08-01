#!/bin/python3

import os 
import sys

def check_reboot():

    return os.path.exists("/run/reboot-required")

def main():

    if check_reboot():
        print("pending reboot")
        sys.exit(1)

    if disk_full():

        print("Disk full")
        sys.exit(1)

    print('everything ok')
    sys.exit(0)

main()
