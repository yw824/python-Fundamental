import csv
import os

def init():
    global dict
    dict = {}
    path = os.path.dirname(__file__)
    f = open(path+"/1_csv.csv", 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        dict[ line[0] ] = line[1] 
    # read complete

init()
for key in dict:
    print(key)