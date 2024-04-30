#########Imports##########
import csv
import random
import sqlite3
import sklearn
from sklearn.preprocessing import MinMaxScaler

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
                x= row[0],row[1],row[3],row[4],row[5],row[6]
                x_data.append(x)
                y = row[2]
                y_data.append(y)
                #print("X values:")
                #print(x)
                #print ("ty")
                #print(y)
    return x_data,y_data


###################################################################
##################### DATA PREPROCESSING ###############################
def dataclenaing(x_data,y_data):
    #take in input should be varaible and the type of data being tested. FOr now its just checking for no values
    #X = dataset.iloc[:, :-1].values Test these versions out see if they work
    #y = dataset.iloc[:, 4].values
    x_cleand=[]
    y_cleand=[]
    for i in len(y_data):
        if y_data[i] ==0: #removing no rain days or hours
            break
        else:
            x_cleand.append(x_data[i])
            y_cleand.append(y_data[i])
    X_train, X_test, y_train, y_test = train_test_split(x_cleand, y_cleand, test_size=0.3, random_state=42) #state = seed of 42:  70/30 split
    return X_train,X_test,y_train,y_test

def datanormilizations(x_train,x_test):
    # feature Normilization
    scaler = MinMaxScaler()
    x_train_norm = scaler.fit_transform(x_train)
    x_test_norm = scaler.transform(x_test)
    return x_test_norm,x_train_norm

def datastandardization(x_train,x_test):
    #datastandardized
    scaler = StandardScaler()
    x_train_std = scaler.fit_transform(x_train)
    x_test_std = scaler.transform(x_test)
    return x_test_std,x_train_std


###################################################################
#################DATABASE SECTION#############################


def SavetoDB():
    import sqlite3
    # Connect to the SQLite database (creates a new one if it doesn't exist)
    conn = sqlite3.connect('example.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    ''')

    # Sample data
    user_data = [
        ('Alice', 'alice@example.com'),
        ('Bob', 'bob@example.com'),
        ('Charlie', 'charlie@example.com')
    ]
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

def savemodel():
    #https://neptune.ai/blog/saving-trained-model-in-python
    return "sucess"

def loadmodel():
    return "Sucess"




