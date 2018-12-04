#!/usr/bin/env python3
import NimStars
import csv
import json
import requests

"""
Creates the result.csv file using the online pakacges.json file and stars.csv file.
"""
def makeResultCsv(username, password):
    packages = requests.get(NimStars.packages_github_url, auth=(username, password)).json()
    with open("stars.csv","r", encoding='utf-8') as csvf:
        reader = csv.DictReader(csvf)
        for row in reader:        
            for package in packages:
                if "url" in package:
                    if(row["project_url"]==package["url"]):
                        package['stars'] = row[' stars']
                        break
    with open("result.csv","w", encoding='utf-8') as result:
        keys = package.keys()
        writer = csv.DictWriter(result, keys)
        writer.writeheader()
        for package in packages:
            data = {key: value for key, value in package.items() if key in keys}
            writer.writerow(data)
    

#############################################################################

if __name__ == "__main__":
    main()
