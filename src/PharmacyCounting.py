import collections
import csv
import datetime
import sys
"""
    This is my submission for the Insight data engineering fellows coding challenge Feb'19
    @author Divya Manjunath
"""
class PharmacyCounting:
    def __init__(self, inputpath,outputpath):
        self.inputpath = inputpath
        self.outputpath = outputpath
    
    def readCSV(self):
        try:
            """
              HashMap to map drug name (key) to Drug object
            """
            drugmap = {}
            """
                Read and parse contents of input file
            """
            with open(self.inputpath, "rt") as csvfile_in:
                    line_reader = csv.reader(csvfile_in)
                    next(line_reader, None)
                    for prescription in line_reader:
                        if prescription:
                            """
                                Checking if 5 columns are present in the row
                            """
                            if (len(prescription) != 5):
                                continue
                            """
                                Assign first element of row as first name
                            """
                            try:
                                firstname = prescription[1].strip().lower()
                            except Exception as e:
                                firstname = ""
                            """
                                Assign second element of row as last name
                            """
                            try:
                                lastname = prescription[2].strip().lower()
                            except Exception as e:
                                lastname = ""
                            """
                                Combining first name and last name for unique identification
                            """
                            prescriber = firstname + lastname
                            """
                                Assign third element as drug key
                            """
                            try:
                                drugname = prescription[3].strip()
                                drugkey =  drugname.strip().lower()
                            except Exception as e:
                                drugname = ""
                                drugkey = ""
                            """
                                Assign fourth element as drug cost
                            """
                            try:
                                drugcost = prescription[4].strip()
                            except Exception as e:
                                drugcost = 0
                            """
                                Add information to HashMap
                            """
                            if drugkey not in drugmap:
                                newdrug = Drug(drugkey)
                                newdrug.setCost(drugcost)
                                newdrug.setCount(1);
                                newdrug.setPrescriber(prescriber)
                                drugmap[drugkey] = newdrug
                            else:
                                olddrug = drugmap[drugkey]
                                olddrug.setCost(olddrug.getCost() + int(drugcost))
                                olddrug.setPrescriber(prescriber)
                                olddrug.setCount(olddrug.getCount() + 1)
            """
                Convert values of drugmap to list  
            """
            druglist = list(drugmap.values())
            """
                Sorting Drug objects by cost, default sort in python (timesort()) used
            """
            druglist.sort(key=lambda x: x.total_cost, reverse=True)
            """
             Writing to output file
            """
            try:
                with open(self.outputpath, mode='w') as csvfile_out:
                    csvfile_out.write("drug_name,num_prescriber,total_cost")
                    for currdrug in druglist:
                        csvfile_out.write(currdrug.toString())
            except Exception as e:
                        print("Unable to write to output file. Exiting!")
 
        except OSError as e:
            print("Please enter valid input file name!")
"""
    Class for Drug object
"""
class Drug:
    """
        Constuctor for Drug class
    """
    def __init__(self, name):
        self.prescriber_set = set()
        self.prescriber_count = 1
        self.total_cost = 0
        self.drug_name = name
    """
        Method to get name of drug
        @return drug name
    """
    def getName(self):
        return self.drug_name
    """
        Method to get cost of drug
        @return total cost
    """
    def getCost(self):
        return self.total_cost
    """
        Method to get count of prescriber
        @return count
    """
    def getCount(self):
        return self.prescriber_count
    """
        Method to return set of prescriber
        @return Set prescriber_set
    """
    def  getPrescribers(self):
        return self.prescriber_set;
    """
        Method to set cost of drug
        @param cost
    """
    def setCost(self,cost):
        self.total_cost = int(cost)
    """
        Method to set count of prescriber
        @param new count
    """
    def setCount(self,newcount):
        self.prescriber_count = int(newcount)
    """
        Method to set prescriber
        @param newprescriber
    """
    def setPrescriber(self,newprescriber):
        return self.prescriber_set.add(newprescriber)
    """
        String representation of Drug class
    """
    def toString(self):
        return ("\n") + (self.drug_name).upper() + (",") + str(self.prescriber_count) + (",") + str(self.total_cost)

def main():
    startTime = datetime.datetime.now()
    if(len(sys.argv) != 3):
        print("Please run with the following arguments: input_file_path, output_file_path")
        return;
    newcounter = PharmacyCounting(sys.argv[1], sys.argv[2])
    newcounter.readCSV()
    endTime = datetime.datetime.now()
    print("Total execution time:%s" %(endTime - startTime))

if __name__ == '__main__':
    main()
