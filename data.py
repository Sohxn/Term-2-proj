import mysql.connector as sql
import os 
key = 'password'
#attempting to connect to server
try:
    
    con = sql.connect(
        host='localhost', 
        database='travel_details',
        user='root',
        password= 'Bobo1403_2004',
       
    )
    print("CONNECTION ESTABLISHED")
    if con.is_connected():
        info = con.get_server_info()
        print("Server version: ",info)
#---------------EXTRACTION FUNCTIONS----------------------
    
    def fetch_cities():
        cursor = con.cursor()
        cursor.execute("SELECT * FROM dest_cities;")
        dest_record = cursor.fetchall()
        des =[]
        for a in range(len(dest_record)):
            des.append(dest_record[a][0])
        return(des)

    def fetch_hotels():
        cursor1 = con.cursor()
        cursor1.execute("SELECT * FROM hotels;")
        hot_record = cursor1.fetchall()
        hot = []
        for b in range(len(hot_record)):
            hot.append(hot_record[b][0])
        return(hot)

    def fill_user(n , e , p):
        cursorop = con.cursor()

    def fetch_airfare(city):
        cursor2 = con.cursor()
        cursor2.execute("SELECT AIR FROM dest_cities WHERE NAME = "+city+";")
        return(cursor2.fetchall())
        
    
    def fetch_railfare(city):
        cursor3 = con.cursor()
        cursor3.execute("SELECT RAIL FROM dest_cities WHERE NAME = ",city)
        
    
    def fetch_roadfare(city):
        cursor4 = con.cursor()
        cursor4.execute("SELECT ROAD FROM dest_cities WHERE NAME = ",city)

        


    

    
except:
    print("ERROR //^~^//")





