import mysql.connector as mysql
import csv
from datetime import datetime

# connect to database
db = mysql.connect(
    host='localhost',
    user='cris',
    passwd='Supper_001',
    database='csv'
)
cursor = db.cursor()

# check if table exist and create table
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
if 'customers' not in tables:
    sql = '''
    CREATE TABLE customers(
        customerid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        companyname VARCHAR(255),
        billingaddress1 VARCHAR(255),
        billingaddress2 VARCHAR(255),
        city VARCHAR(255),
        state VARCHAR(255),
        postalcode VARCHAR(255),
        country VARCHAR(255),
        phonenumber VARCHAR(255),
        emailaddress VARCHAR(255) NOT NULL UNIQUE,
        createddate DATETIME
        )
    '''
    cursor.execute(sql)

# read csv file and store to mysql
csv_file = open('customer.csv', 'r')
reader = csv.reader(csv_file)
init = True
for line in reader:
    if init:
        init = False
        continue
    query = '''INSERT INTO customers(customerid, firstname, lastname,
                                companyname, billingaddress1,
                                billingaddress2, city, state,
                                postalcode, country, phonenumber,
                                emailaddress, createddate)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    line[0] = int(line[0])
    line[-1] = datetime.strptime(line[-1], '%d/%m/%Y %H:%M')
    values = tuple(line)
    cursor.execute(query, values)
    db.commit()
