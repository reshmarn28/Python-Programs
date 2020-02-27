import mysql.connector
mydb = mysql.connector.connect (
    host="localhost",
    user="root",
    passwd="admin",
    database="world"
)
mycursor = mydb.cursor()

"""# # create table
mycursor.execute("CREATE TABLE abc (name VARCHAR(255), marks VARCHAR(255))")
print("Table is created...")"""

# # Insert into table
sql = "INSERT INTO (name, marks) VALUES (%s, %s)"
val = ("PQR", "90")
mycursor.execute(sql, val)
mydb.commit()
print("data inserted...")