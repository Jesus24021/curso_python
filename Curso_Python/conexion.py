import mysql.connector

conexion = mysql.connector.connect(user='root', 
                                   password='',
                                   host='localhost',
                                   database='ferreteria',
                                   port='3306')

print(conexion)


