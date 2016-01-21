#!/usr/bin/env python
""" This program reads the database file and computes the number of records 
    that contain the exact case insenstive string strPattern. 
"""

def findDuplicate(db, strPattern):
      
    with open(db, 'r') as f:
        allLines = f.readlines()

    strPattern = strPattern.lower()

    count = 0 
    # search each line for strPattern
    for line in allLines:
        singleLine = ' '.join(line.split())
        singleLine= singleLine.lower()
        if singleLine.find(strPattern) > -1:
            count += 1

    # return the number of occurances of strPattern in dbsales
    return count; 

print findDuplicate("iowa-liquor-sample.csv", "single malt scotch") 
