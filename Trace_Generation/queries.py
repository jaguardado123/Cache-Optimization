import pyodbc
import time
import random

# SQL Server credentials
server = 'DESKTOP-7OQL1C2'
password = 'test'   
driver= '{ODBC Driver 17 for SQL Server}'

###########################################
# Database | Table               | Rows   #
###########################################
# CabRides | cab_rides           | 30,000 #
# Students | StudentsPerformance | 6,000  #
# Telecom  | telecom_users       | 6,300  #
# Weather  | weather             | 6,300  #
###########################################

# Array of SQL commands to be randomly selected.
query=[
    "select * from CabRides.dbo.cab_rides",
    "select * from Students.dbo.StudentsPerformance",
    "select * from Telecom.dbo.telecom_users",
    "select * from Weather.dbo.weather",
    "use CabRides select top 1000 * from cab_rides where name='Lyft'",
    "use Students select top 1000 * from StudentsPerformance where gender='male'",
    "use Telecom select top 1000 * from telecom_users where InternetService='DSL'",
    "use Weather select top 1000 * from weather where location='Fenway'",
    "insert into CabRides.dbo.cab_rides values (0.44, 'Lyft', 1540000000000, 'North Station', 'Haymarket Square', 16.5, 1, 'e8bac1d1-6e83-4ebd-a0a9-bfcf9de1a86f', 'lyft_line', 'UberX')",
    "insert into Students.dbo.StudentsPerformance values ('female', 'group B', 'bachelors degree', 'standard', 'completed', 72, 80, 94)",
    "insert into Telecom.dbo.telecom_users values (6780, '7010-BRBUU', 'Male', 0, 'Yes', 'No', 75, 'Yes', 'No', 'DSL', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Two Year', 'Yes', 'Credit card', 24.2, 3370.2, 'No')",
    "insert into Weather.dbo.weather values (42.45, 'Fenway', 1, 1012.17, 0.1089, default, 0.96, 1.53)",
    "delete top (1) from CabRides.dbo.cab_rides where name='Lyft'",
    "delete top (1) from Students.dbo.StudentsPerformance where gender='male'",
    "delete top (1) from Telecom.dbo.telecom_users where InternetService='DSL'",
    "delete top (1) from Weather.dbo.weather where location='Fenway'"
]

user=[
    "temp",
    "temp2",
    "temp3",
    "temp4",
    "temp5",
    "temp6",
    "temp7",
    "temp8",
    "temp9",
    "temp10",
]
max = 100
for u in range(0, 9):
    # Connect to SQL server.
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;UID='+user[u]+';PWD='+ password) as conn:
        with conn.cursor() as cursor:

            # Make 300 randomized queires to SQL server from query array.
            queries = random.randint(25, max)
            for x in range(0, queries):
                i = random.randint(0,15)
                cursor.execute(query[i])
                time.sleep(2) # Pause for 2 seconds