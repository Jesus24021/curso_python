import mysql.connector

conexion = mysql.connector.connect(user='root', 
                                   password='',
                                   host='localhost',
                                   database='peliculas',
                                   port='3306')

print(conexion)