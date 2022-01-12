import mysql.connector as sql
import os 
key = 'password'
#attempting to connect to server
try:
    con = sql.connect(
        host='localhost',
        user='root',
        password= 'bobo14032004',
        database='travel_details'
    )
    print("CONNECTION ESTABLISHED")
    if con.is_connected():
        info = con.get_server_info()
        print("Server version: ",info)
    cursor = con.cursor()
    show = cursor.execute("SHOW DATABASES")
    
except:
    print("CONNECTION FAILED")




