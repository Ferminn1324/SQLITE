import sqlite3

conexion = sqlite3.connect ("Ejemplo.db")

c= conexion.cursor()

movimientos = [('10/febrero/2013', 'ventana', 'HPC', 50, 20.01),('11/febrero/2013', 'compra', 'SNY', 100, 7.18), ('6/nov/2014', 'compra', 'XBX', 75,5.33)]

c. executemany ('INSERT INTO acciones VALUES (?,?,?,?,?)', movimientos)

conexion.commit ()

for row in c.execute("SELECT * FROM acciones WHERE operacion ='compra'"):
    print (row)

    conexion.close


#for row in c.execute("SELECT * FROM acciones "):
    #print(row)

    #conexion.close