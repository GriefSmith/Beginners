import os
import mysql.connector
import time

# Sleep to ensure MySQL is ready
time.sleep(5)

# Connect to the database
db = mysql.connector.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)

cursor = db.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
)
""")

# Insert data into the table
cursor.execute("INSERT INTO test_table (name) VALUES (%s)", ('Test Name',))

# Commit the transaction
db.commit()

# Query the data from the table
cursor.execute("SELECT * FROM test_table")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print('row:  \n\n\n')
    print(row)

# Close the connection
cursor.close()
db.close()
