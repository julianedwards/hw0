#!/usr/bin/env python
""" this program reads the database file and computes the number of records that contain 
    the exact case insenstive phrase "single malt scotch"
"""

def findDuplicate(dbsales, strPattern):
      
    with open(dbsales, 'r') as f:
        sales = f.readlines()

    strPattern = strPattern.lower()

    count = 0 
    # search each line for strPattern
    for line in sales:
        singleSale = ' '.join(line.split())
        singleSale = singleSale.lower()
        if singleSale.find(strPattern) > -1:
            count += 1

    # return the number of occurances of strPattern in dbsales
    return count; 

print findDuplicate("iowa-liquor-sample.csv", "single malt scotch") 
