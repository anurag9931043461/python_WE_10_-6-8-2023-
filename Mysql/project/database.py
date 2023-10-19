import mysql.connector as sql

try:
    krishna=sql.connect(host="localhost",port=3306,user="root",password="root",db="we10")
    car=krishna.cursor()
except:
    print("Connection failed")
else:
    print("database connected")

