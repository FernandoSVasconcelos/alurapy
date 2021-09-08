# -*- coding: utf-8 -*-
from connection_factory import Connection_factory

connection=Connection_factory().get_connection()

cursor = connection.cursor()
cursor.execute('SELECT * from cursos')

for linha in cursor:
    print(f"{linha}")

connection.close()