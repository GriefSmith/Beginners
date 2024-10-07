
import os
import mysql.connector

db = mysql.connector.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)
 ⁠ print("|||||||||||||||||||||||||||||||" dir(db)) ⁠