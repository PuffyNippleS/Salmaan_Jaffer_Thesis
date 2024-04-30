#########Imports##########
import csv
import random

################ ###################
###### DATA PREPROCESSING ##########
def read_csv():
    file_path="Dataset/Temp dataset.csv"
    data = []
    x_data = []
    y_data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            #print(row)
            if row[0]!='': #Data Cleaning
                #print("added")
                x= row[0],row[1],row[3],row[4],row[5],row[6]
                x_data.append(x)
                y = row[2]
                y_data.append(y)
              #  print("X values:")
               # print(x)
                #print ("ty")
                #print(y)
    return x_data

def dataclenaing(inpt):
    #take in input should be varaible and the type of data being tested. FOr now its just checking for no values
    for i in inpt:
        if i[3]==0:
            break
        else:
            return i

def datanormilizations():
    return "test"

def standardization():
    return "Complete"

def datainput():
    return "test"


def SavetoDB():
    return "success"

def readfromDB():
    return "success"

def savemodel():
    #https://neptune.ai/blog/saving-trained-model-in-python
    return "sucess"

def loadmodel():
    return "Sucess"

csv_file = read_csv()
print(csv_file[1])
print(csv_file[2])



