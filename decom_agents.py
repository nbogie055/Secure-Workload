#!/usr/bin/env python

'''
   This script will decom tetration agents

    File name: modify_agents.py
    Version: 1
    Author: Nicholas Bogdajewicz
    Date created: 7/14/2022
    Date last modified: 7/20/2022
    Python Version: 3.8.2
    requests version: 2.27.0
'''

import cluster_login
from tetpyclient import RestClient
import json
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():

    login = cluster_login.cluster_login()
    host = login[0]
    TET_API_KEY = login[1]
    TET_SEC = login[2]
    agent = login[3]

    if agent == None:
        while True:
            agent = input("Please enter an agent's hostname: ")
            while True:
                ans = input("You entered " + agent + " is this correct? (y or n): ")
                ans_low = ans.lower()
                if ans_low != "y" and ans_low != "n":
                    print("Please enter y or n.")
                    continue
                else:
                    break
            if ans_low == "n":
                continue
            else:
                break

    agent =  agent.split(",")

    offset = ""
    while True:

        #gets all of the sensors
        restclient = RestClient(host,
                                api_key=TET_API_KEY,
                                api_secret=TET_SEC,
                                verify=False)

        response = restclient.get("/sensors?limit=1000&offset=" + offset)

        response_json = json.loads(response.text)
        if "offset" in response_json:
            offset = response_json["offset"]

        #loops through sensors to find the uuid of your hostname
        for item in response_json["results"]:
            if item["host_name"] in agent:
                UUID = item["uuid"]
                while True:
                    ans = input("Are you sure you want to decommission " + item["host_name"] + "? (y or n): ")
                    ans_low = ans.lower()
                    if ans_low != "y" and ans_low != "n":
                        print("Please enter y or n.")
                        continue
                    else:
                        break

                if ans_low == "n":
                    continue

                #Removes the agent based on the UUID
                restclient = RestClient(host,
                                        api_key=TET_API_KEY,
                                        api_secret=TET_SEC,
                                        verify=False)

                response = restclient.delete("/sensors/" + UUID)
                if response.status_code == 204 or response.status_code == 200:
                    print("Successfully decommissioned host " + item["host_name"] + ".")
                    continue
                else:
                    print("Error " + str(response) + "! Could not delete agent " + item["host_name"])
                    continue

        if "offset" not in response_json:
            break

if __name__ == '__main__':
    main()

