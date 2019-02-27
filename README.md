## Table of Contents

1. [Dependencies and running instructions](#Dependencies-and-running-instructions)
2. [Approach](#Approach)
3. [Data structures](#Data-Structures)
4. [Complexity analysis](#Complexity-analysis)

## Dependencies and running instructions

1. The source code PharmacyCounting.py is written in Python 3.7.1 and resides in src folder 
2. The instructions to run are specified in run.sh file
3. Imports required are mentioned alongside: import collections import csv import datetime import sys

## Approach

1. Create "Drug" class to store drug name, number of prescribers, total cost and set of unique prescribers (stored in Python Set)
2. Intialize a python dictionary, use drug name as the key, map key to Drug object
3. Loop through each line of input file and check for presence of drug key 
   - If key not present<br />
     intialize a new "Drug" class object and set its attributes
   - If key present<br />
     update total cost<br />
     check if prescriber is present in set if not update count
4. Convert all the values in dictionary to list, sort based on total_cost (default sort() implements Timesort())
7. Append string representation defined in "Drug" class of sorted list to output file
## Data structures

1. Dictionary to map key (drug name) to "Drug" object
2. Set to store unqiue prescribers
3. List to sort Dictionary values.

## Complexity analysis

1. Assume number of records in input file is N, with M unique drugs (length of each record is << number of records)
2. Looping through input file takes O(N) , lookup in dictionary and adding to Set takes O(1) each
3. Sorting "Drug" objects by cost takes O(Mlog(M))
4. Writing "Drug" objects to file takes O(M)
5. Overall time complexity is Max(O(N), O(Mlog(M)))
6. Assuming there are M unique drugs and P unique prescribers for each drug, the space complexity is O(M * P)
