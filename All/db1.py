import mysql.connector
mydb = mysql.connector.connect(host = "127.0.0.1",
                            user = "root",
                            passwd = "admin", 
                            database = "gns")
mycursor = mydb.cursor()

#create table
# mycursor.execute("create table employee(name VARCHAR(255), email VARCHAR(255))")
# print("table is created")

#insert into table
# sql = "insert into employee (name, email) values (%s,%s)"
# val = ("gns","gns@gmail.com")
# mycursor.execute(sql, val)
# mydb.commit()
# print("data inserted")

#select from table
# mycursor.execute("select * from employee")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

#where clause
# sql = "select * from employee where email = 'abc@gmail.com'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

#Delete
sql = "delete from employee where name='abc'"
mycursor.execute(sql)
print("table updated")
mycursor.execute("select * from employee")
myresult = mycursor.fetchall()
print(myresult)
