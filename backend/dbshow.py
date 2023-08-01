# Importing module
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
	host = "localhost",
	user = "ezhilr",
	password = "pass"
)

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()
 
# Show database
cursor.execute("SHOW DATABASES;")
 
for x in cursor:
  print(x)