#!/usr/bin/env python

'''
   This script will contain login info for each secure workload cluster

    File name: cluster_login.py
    Version: 1
    Author: Nicholas Bogdajewicz
    Date created: 7/15/2022
    Date last modified: 7/15/2022
'''

import sys
import argparse

def cluster_login():

    #takes fabric argument and store the corresponding url
    parser = argparse.ArgumentParser(description='Example: python3 script_name.py --fabric prod1 --user admin --pass \'cisco!23\' --chg CHG12345')
    parser.add_argument("--fabric", dest="fabric", metavar='', type=str, help='Choose Fabric: lab, prod1, prod2')
    parser.add_argument("--host", dest="host", metavar='', type=str, help='Enter hostname')
    args = parser.parse_args()
    site = args.fabric
    hostname = args.host

    if site == None:
        while True:
            site = input("Input secure workload cluster (lab, prod1, prod2): ")
            if site.lower() == "lab" or site.lower() == "prod1" or site.lower() == "prod2":
                answer = input("Are you sure you want to select " + site + "? (y or n): ")
                if answer.lower() == "y":
                    break
                else:
                    continue
            else:
                print("\nPlease input a valid fabric (lab, prod1, prod2): ")
                continue

    while True:
        if site.lower() == "lab":
            url = ""
            TET_API_KEY = ""
            TET_SEC = ""
            break
        elif site.lower() == "prod1":
            url = ""
            TET_API_KEY = ""
            TET_SEC = ""
            break
        elif site.lower() == "prod2":
            url = ""
            TET_API_KEY = ""
            TET_SEC = ""
            break
        else:
            print("Could not determine the fabric.")
            sys.exit()

    return(url, TET_API_KEY, TET_SEC, hostname)
