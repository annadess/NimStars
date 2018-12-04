#!/usr/bin/env python3
import requests
import json
import getpass
import CheckDuplicates
import CreateUpdatedCSV

packages_github_url = "https://raw.githubusercontent.com/nim-lang/packages/master/packages.json"
github_user_url = "https://api.github.com/user"

"""
Resolves urls into uniform formats, and creates the Github API url.
"""
def reworkUrl(url):
    res = ''
    if "git@" in url:
        res = url.replace(":","/").replace("git@","https://").replace(".git","").replace("github.com","api.github.com/repos")
    elif("//github.com" in url):
        res = url
        if res[-1] == "/":
            res = res[:-1]
        res = res.replace(".git","").replace("github.com","api.github.com/repos")
    return res

"""
Checks if request has been successful.
"""
def isOkay(request):
    return request.status_code >= 200 and request.status_code < 300

"""
Creates the stars.csv file and populates it with repository urls and star counts.
"""
def writeCsv(username, password):
    dupes = CheckDuplicates.runCheck(username, password)
    packages = requests.get(packages_github_url, auth=(username, password)).json()
    with open("stars.csv","w") as csvf:    
        csvf.write("project_url, stars\n")
        for package in packages:
            if "url" in package:
                if package["url"] in dupes:
                    dupes.remove(package["url"])
                    continue
                url = reworkUrl(package["url"])
                if url != '':
                    request = requests.get(url, auth=(username, password))
                    if isOkay(request):
                        stars = request.json()["stargazers_count"]
                        csvf.write(f"{package['url']}, {stars}\n")

def main():
    print("Welcome to NimStars!")
    print("For the sake of overcoming Github's API rate-limit, please login:")
    username = input("Github username: ")
    password = getpass.getpass("password: ")
    r = requests.get(github_user_url, auth=(username, password))
    if isOkay(r):
        print("Login Successful!")
        print("Getting Stars...")
        writeCsv(username, password)
        print("Done!")
        print("Creating result.csv ...")
        CreateUpdatedCSV.makeResultCsv(username, password)
        print("All Done!")
    else:
        print("Login Failed. Exiting program.")

#############################################################################

if __name__ == "__main__":
    main()