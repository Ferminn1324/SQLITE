import sqlite3

conexion = sqlite3.connect('Ejemplo.db')


c = conexion.cursor()

c. execute ('''CREATE TABLE acciones ( fecha text, operacion text, simbolo text, cantidad real, precio real)''')

c.execute("INSERT INTO acciones VALUES ('3/marzo/2022','venta','INV',100,10)")

c.execute("INSERT INTO acciones VALUES ('10/mayo/2044','compra','INV',444,4)")

c.execute("INSERT INTO acciones VALUES ('11/diciembre/1998','rembolso','INV',500,5)")

c.execute("INSERT INTO acciones VALUES ('24/junio/2003','compra','INV',666,6)")

c.execute("INSERT INTO acciones VALUES ('5/abr/1900','venta','INV',999,9)")

c.execute("INSERT INTO acciones VALUES ('9/nov/2005','compra','INV',444,4)")


conexion.commit()

conexion.close()
