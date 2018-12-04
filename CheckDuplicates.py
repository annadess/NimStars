#!/usr/bin/env python3
import requests
import json
import getpass
import NimStars

"""
Returns a list of repositories which are appearing twice in the packages.json file.
"""
def runCheck(username, password):
    packages = requests.get(NimStars.packages_github_url, auth=(username, password)).json()
    urllist = []
    dupe = []
    for package in packages:
        if "url" in package:
            urllist.append(package["url"])
    urllist.sort()
    for i in range (len (urllist) -1):
        if urllist[i] == urllist[i+1]:
            dupe.append(urllist[i])
    return dupe

def main():
    print("Welcome to the CheckDuplicates script of NimStars!")
    print("For the sake of overcoming Github's API rate-limit, please login:")
    username = input("Github username: ")
    password = getpass.getpass("password: ")
    r = requests.get(NimStars.github_user_url, auth=(username, password))
    if NimStars.isOkay(r):
        print("Login Successful!")
        dupe = runCheck(username, password)
        if len(dupe) != 0:
            print("There were duplicates found")
            print(dupe)
        else:
            print("No duplicates were found")
    else:
        print("Login Failed. Exiting program.")

#############################################################################

if __name__ == "__main__":
    main()