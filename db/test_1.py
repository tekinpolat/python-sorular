# ilişkisel database --> Mysql, Postgresql, Oracle, MsSQL, Sqlite, MariaDb,
# ilişkisel Olmayan database(Nosql) --> MongoDB, Redis, Cassandra, Couchbase
# SQL 

#Sql  CRUD 
#C --> Create 
#R --> Select(Read) 
#U --> Update 
#D --> Delete 


"""
    MySQL Connector Python.
    PyMySQL.
    MySQLDB.
    MySqlClient.
    OurSQL.
"""

import mysql.connector

mydb = mysql.connector.connect(
    database="mervan",
    host="localhost",
    user="root",
    password="Tknplt21.",
    auth_plugin='mysql_native_password'
)

print(mydb)


