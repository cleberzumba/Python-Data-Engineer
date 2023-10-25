
# Here I will import four modules from the Python library
import csv
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Here i will create Database connection data
host = "localhost"
port = "5432"
database = "postgresDB"
user     = "dbadmin"
password = "xxxxxxxxxx"

# NOTE: I know that you shouldn't put the database password in the code, but as I'm just making a demo code I will leave the password here.

try:
    # here I will create connection to the database
    print("\nConnecting to the PostgreSQL...")
    connection = psycopg2.connect(host=host,
                                  port=port,
                                  database=database,
                                  user=user,
                                  password=password)

    print("\nConnection made successfully!")

    # I will create a cursor object which is a method of the connection and is used to execute SQL queries against the database this open a cursor to oonnect to the database.
    cursor = connection.cursor()

    # now I will create the CANDIDATES table in the postgreSQL database
    print("\nCreating Table...")
    command_sql = '''CREATE TABLE CANDIDATES("First Name" varchar(30), 
                                             "Last Name" varchar(40), 
                                             Email varchar(90), 
                                             "Application Date" date, 
                                             Country varchar(60), 
                                             YOE integer, 
                                             Seniority varchar(30), 
                                             Technology varchar(50), 
                                             "Code Challenge Score" integer, 
                                             "Technical Interview Score" integer)'''
    cursor.execute(command_sql)

    # here I will open the file specified by the path contained in the input variable in read mode ('r')
    # and starts a for loop that iterates over the data elements.
    # I will insert the data into the database with the insert command below
    input = 'D:/tmp/candidates.csv'

    with open(input, 'r') as f:
        data = csv.DictReader(f, delimiter=';')
        print("\Inserting table...")
        for row in data:
            query = '''INSERT INTO CANDIDATES("First Name", "Last Name", Email, "Application Date", Country, YOE, Seniority, Technology, "Code Challenge Score", "Technical Interview Score") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
            values = (row['First Name'], row['Last Name'], row['Email'], row['Application Date'], row['Country'], row['YOE'],
                      row['Seniority'], row['Technology'], row['Code Challenge Score'], row['Technical Interview Score'])

            cursor.execute(query, values)

    # first exploratory data analysis
    # a SQL query that selects the total number of hires by technology from the candidates table in the database.
    query = '''SELECT Technology, count(*) as total
               FROM dbadmin.candidates
               GROUP BY 1
               ORDER BY 2 DESC'''

    df = pd.read_sql_query(query, connection)



    # second exploratory data analysis
    # a SQL query that selects the total number of hires per year from the candidates table in the database.
    # I use the RANK window function to perform the calculation that will return the total number of hires for each year.
    query2 = '''SELECT year, total,
                       RANK() OVER (ORDER BY year DESC) as rank
                FROM (SELECT TO_CHAR("Application Date", 'YYYY') as year, count(*) as total
                      FROM dbadmin.candidates
                      GROUP BY 1) as subquery
                ORDER BY year DESC;'''

    df2 = pd.read_sql_query(query2, connection)



    # third exploratory data analysis
    # an SQL query that selects the total number of hires by seniority from the candidates table in the database.
    query3 = '''SELECT seniority, count(*)
                FROM dbadmin.candidates
                GROUP BY 1;'''

    df3 = pd.read_sql_query(query3, connection)



    # fourth and final exploratory data analysis
    # a SQL query that selects the total number of hires by country over the years from the candidates table in the database.
    # only the countries Colombia, Brazil, Ecuador, United States of America
    query4 = '''SELECT country, TO_CHAR("Application Date", 'YYYY') as year, count(*)
                FROM dbadmin.candidates
                WHERE country IN ('Colombia', 'Brazil', 'Ecuador', 'United States of America')
                GROUP BY 1,2
                ORDER BY 2 DESC;'''

    df4 = pd.read_sql_query(query4, connection)


    # I will confirm changes made to the database
    connection.commit()
    print("\nData loaded successfully!!")

    # I will close the database connection
    cursor.close()
    connection.close()


    # here I will use the Matplotlib library to create a pie chart.
    labels = df['technology']
    sizes = df['total']
    colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.show()


    # here I will also use the Matplotlib library to create a horizontal bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(df2['year'], df2['total'])
    plt.xlabel('Total Hires')
    plt.ylabel('Year')
    plt.title('Total de Hires per Year')
    plt.gca().invert_yaxis()
    plt.show()

    # I will also use the Matplotlib library to create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df3['seniority'], df3['count'])
    plt.xlabel('seniority')
    plt.ylabel('Total Candidates')
    plt.title('Total Candidates by Seniority')
    plt.xticks(rotation=45)
    plt.show()

    # here I will also use the Matplotlib library to create a multi-line bar chart
    plt.figure(figsize=(12, 6))
    countries = df4['country'].unique()

    for country in countries:
        data = df4[df4['country'] == country]
        plt.plot(data['year'], data['count'], marker='o', linestyle='-', label=country)

    plt.xlabel('Year')
    plt.ylabel('Total Candidates')
    plt.title('Total Candidates by year and Country')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

# I finish the code with exception handling in case an error occurs when connecting to a PostgreSQL database and i'm using the psycopg2 library
except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)


