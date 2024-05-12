#########Imports##########
import csv
import random
import sqlite3
import mysql.connector
import sklearn
import numpy
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import os
import joblib

################ ###################
###### DATA INPUT ##########
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
                x=row[1],row[3],row[4],row[5]
                x_data.append(x)
                y = row[2]
                y_data.append(y)
                #print("X values: "+ str(x))
                #print ("y: "+ str(y))
    return x_data,y_data


###################################################################
##################### DATA PREPROCESSING ###############################
def dataclenaing(x_data,y_data):
    #take in input should be varaible and the type of data being tested. FOr now its just checking for no values
    #X = dataset.iloc[:, :-1].values Test these versions out see if they work
    #y = dataset.iloc[:, 4].values
    x_cleand=[]
    y_cleand=[]
    k=0
    k = len(y_data)
    #print(k)
    i=1 #Skip first line as we dont need heading.
    while i <k:
        #print(i)
        if y_data[i]!= "0": # Cleaning 0 data to prevent scewing/ favoring no rain
            x_cleand.append(x_data[i])
            y_cleand.append(y_data[i])
        i = i + 1
    x_cleandflt=[]
    y_cleandflt=[]
    for i in y_cleand: #Converting to float
        y=float(i)
        y_cleandflt.append(y)
    for i in x_cleand:
        x = float(i[0]), float(i[1]), float(i[2]), float(i[3])
        x_cleandflt.append(x)
        print(x)
    X_train, X_test, y_train, y_test = train_test_split(x_cleandflt, y_cleandflt, test_size=0.3, random_state=42) #state = seed of 42:  70/30 split
    return X_train,X_test,y_train,y_test

def datanormilizations(x_train,x_test):
    # feature Normilization
    x_train1 = [row[1:] for row in x_train]
    #for i in x_train1:
     #   print(i)
    x_test1=[row[1:] for row in x_test] #removing first row
    scaler = MinMaxScaler()
    x_train_norm = scaler.fit_transform(x_train1)
    x_test_norm = scaler.transform(x_test1)
    return x_test_norm,x_train_norm

def datastandardization(x_train,x_test):
    #datastandardized
    scaler = StandardScaler()
    x_train_std = scaler.fit_transform(x_train)
    x_test_std = scaler.transform(x_test)
    return x_test_std,x_train_std


###################################################################
#################DATABASE SECTION#############################sdok;jfdhaklsjdhfklajsdhflkjashdkljafhkl


def SavetoDB():
    import sqlite3
    # Connect to the SQLite database (creates a new one if it doesn't exist)
    conn = sqlite3.connect('example.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # Create a table if it doesn't exist
    # Sample data
    # Insert data into the table
    cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', user_data)
    # Commit changes to the database
    conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()
    return "success"

def readfromDB():
    # Connect to the SQLite database
    conn = sqlite3.connect('Save.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # SELECT query to retrieve data from the users table
    cursor.execute('SELECT * FROM users')
    # Fetch all rows from the result of the SELECT query
    rows = cursor.fetchall()
    # Print the retrieved data
    for row in rows:
        print(row)
    # Close the cursor and connection
    cursor.close()
    conn.close()

    return "success"


####################################################
##############MODEL SAVING##########################
def savemodel(model, type):
    if type ==1:
        # Assuming 'knn' is your trained KNeighborsClassifier model
        model_folder_path = '/Model'  # Specify the folder path where you want to save the model
        os.makedirs(model_folder_path, exist_ok=True)  # Create the folder if it doesn't exist
        model_file_path = os.path.join(model_folder_path, 'KNN.pkl')  # Specify the file path and name
        joblib.dump(model, model_file_path)
        return "Sucess"
    elif type == 2:
        # Assuming 'knn' is your trained KNeighborsClassifier model
        model_folder_path = '/Model'  # Specify the folder path where you want to save the model
        os.makedirs(model_folder_path, exist_ok=True)  # Create the folder if it doesn't exist
        model_file_path = os.path.join(model_folder_path, 'MLR.pkl')  # Specify the file path and name
        joblib.dump(model, model_file_path)
        return "Sucess"
    return "False"
def loadmodel(type):
    if type ==1:
        model_folder_path = '/Model'  # Specify the folder path where you want to save the model
        os.makedirs(model_folder_path, exist_ok=True)  # Create the folder if it doesn't exist
        model_file_path = os.path.join(model_folder_path, 'KNN.pkl')  # Specify the file path and name
        KNN = joblib.load(model_file_path)
        return KNN
    elif type == 2:
        # Assuming 'knn' is your trained KNeighborsClassifier model
        model_folder_path = '/Model'  # Specify the folder path where you want to save the model
        os.makedirs(model_folder_path, exist_ok=True)  # Create the folder if it doesn't exist
        model_file_path = os.path.join(model_folder_path, 'MLR.pkl')  # Specify the file path and name
        MLR = joblib.load(model_file_path)
        return MLR
    return "NULL"



###############################################################
#########RUNNING##############################################
def main():
    x,y=read_csv()
    X_train, X_test, y_train, y_test = dataclenaing(x,y)
    x_test_norm,x_train_norm=datanormilizations(X_train,X_test)
    return x_test_norm,x_train_norm,y_train,y_test


