import mysql.connector
mydb = mysql.connector.connect(host = "127.0.0.1",
                            user = "root",
                            passwd = "admin", 
                            database = "abc")
mycusrsor = mydb.cursor()

#create table
# mycusrsor.execute("create table table1(name VARCHAR(255), email VARCHAR(255))")
# print("table is created")

#insert into table
# sql = "insert into table1 (name, email) values (%s,%s)"
# val = ("xyz", "xyz@gmail.com")
# mycusrsor.execute(sql, val)
# mydb.commit()
# print("data inserted")

# #select from table
# mycusrsor.execute("select * from table1")
# m1 = mycusrsor.fetchall()
# #myresult = mycusrsor.next()
# for x in m1:
#     print(x)

#where clause
sql = "select * from table1 where email = 'pqr@gmail.com'"
mycusrsor.execute(sql)
myresult = mycusrsor.fetchall()
for x in myresult:
    print(x)

# #Delete
# sql = "delete from python where name = 'pqr'"
# mycusrsor.execute(sql)
# print("Data deleted")

# mycusrsor.execute("select * from python")
# myresult = mycusrsor.fetchall()
# for x in myresult:
#     print(x)

