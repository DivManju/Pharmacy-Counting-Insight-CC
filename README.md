## Table of Contents

1. [Dependencies and running instructions](#Dependencies-and-running-instructions)
2. [Approach](#Approach)
3. [Data structures](#Data-Structures)
4. [Complexity analysis](#Complexity-analysis)

## Dependencies and running instructions

1. The source code PharmacyCounting.py is written in Python 3.7.1 and resides the src folder. 
2. The instructions to run are specified in the run.sh file
3. The following imports are required in the code: import collections import csv import datetime import sys

## Approach

1. A private Drug class was used for storing relevant information such as drug name, number of prescribers, total cost and a set of unique prescribers
2. A python dictionary was created which mapped a drug key to the Drug object. The drug key was the drug name, which was stripped of extraneous spaces and cast to lower case
3. Reading through the input file line-by-line, the dictionary was checked for the presence of the key generated from each drug name
4. If the map did not contain the key, a new Drug object was created and the fields of the new drug object such as cost, number of prescribers and Set of prescribers was initialized
5. If the map contained the key, the cost was updated and the Set was checked for the existence of the prescriber. If the prescriber did not exist, the prescriber was added to the Set and the count was updated
6. After parsing the entire input file, the values of the dictionary were stored in an list, which was then sorted according to total_cost using the default sort() function of python which implements Timesort()
7. The sorted list was appended to the output file, the String representation of each Drug object in the list (defined in Drug class) was used for writing to output file

## Data structures

1. Dictionary to map drug name (key) to Drug object.
2. Set to ensure the same prescriber is not counted twice.
3. List to sort Dictionary values for sorting.

## Complexity analysis

1. Assume that the number of records in the input file is N, with M unique drugs. Assumption: length of each record is << number of records
2. Parsing the file and storing each drug in the Dictionary takes O(N) time, adding and lookup in dictionary, adding to Set each takes O(1) time
3. Sorting the Drug objects by cost takes O(Mlog(M)) time
4. Writing the Drug objects to file takes O(M) time
5. Overall time complexity is Max(O(N), O(Mlog(M)))
6. Assuming there are M unique drugs and P unique prescribers for each drug, the space complexity is O(M * P)
