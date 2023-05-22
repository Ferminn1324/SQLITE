from tkinter import *
from tkinter import ttk
from tkinter import Tk
import tkinter as tk
import csv
import sqlite3


class Fuente:
    def __init__(self):
       self.raiz = Tk()

       self.raiz.title("Muestra Widgets")

       self.Nombre = StringVar()
       self.APaterno = StringVar()
       self.AMaterno = StringVar()
       self.Correo = StringVar()
       self.movil = StringVar()
       self.estado = StringVar()
       self.ocupacion = StringVar()
       self.aficion = StringVar()
       self.aficionn = StringVar()
       self.aaficion = StringVar()
       self.leer = StringVar()
       self.musica = StringVar()
       self.videojuegos = StringVar()
       self.estudiante = StringVar()
       self.empleado  = StringVar()
       self.desempleado = StringVar()
       self.guardar = StringVar()
       self.cancelar = StringVar()

     

       mainFrame = ttk.Frame(self.raiz,padding=" 15 15 15 15")
       mainFrame.grid(column=0,row=0)

       mainFramee = ttk.Frame(mainFrame,padding="15 15 15 15",relief="raised")
       mainFramee.grid(column=0,row=0,sticky=(W))

       mainFrame3 = ttk.Frame(mainFrame,padding="38 15 38 15",relief="raised")
       mainFrame3.grid(column=0,row=1,pady=20,sticky=(W))

       mainFrame4 = ttk.Frame(mainFrame,padding="15 15 15 15")
       mainFrame4.grid(column=1,row=0,sticky=(W))

#Framee
       self.Nombre = ttk.Entry(mainFramee, width=40, textvariable=self.Nombre)
       self.Nombre.grid(column=1,row=0)
       self.APaterno = ttk.Entry(mainFramee, width=40, textvariable=self.APaterno)
       self.APaterno.grid(column=1,row=1)
       self.AMaterno = ttk.Entry(mainFramee, width=40, textvariable=self.AMaterno)
       self.AMaterno.grid(column=1, row=2)
       self.Correo = ttk.Entry(mainFramee, width=40,textvariable=self.Correo)
       self.Correo.grid(column=1,row=3)
       self.movil = ttk.Entry(mainFramee,width=40,textvariable=self.movil)
       self.movil.grid(column=1,row=4)

       ttk.Label(mainFramee, text="Nombre:").grid(column=0, row=0,pady=20)
       ttk.Label(mainFramee, text="A.Paterno:").grid(column=0, row=1,pady=20)
       ttk.Label(mainFramee, text="A.Materno:").grid(column=0, row=2,pady=20)
       ttk.Label(mainFramee, text="Correo:").grid(column=0, row=3,pady=20)
       ttk.Label(mainFramee, text="Movil:").grid(column=0, row=4,pady=20)
#MAINFRAME3
       ttk.Label(mainFrame3,text="Aficiones:").grid(column=0,row=0,sticky=(W))

       ttk.Checkbutton(mainFrame3,text="Leer:",variable=self.aficion).grid(column=0, row=1, sticky=(W),padx=10)
       ttk.Checkbutton(mainFrame3,text="Musica:",variable=self.aficionn).grid(column=1,row=1,sticky=(W),padx=10)
       ttk.Checkbutton(mainFrame3,text="Videojuegos:",variable=self.aaficion).grid(column=2,row=1,sticky=(W),padx=10)

       ttk.Button(mainFrame,text="Guardar",command=self.guardarLista).grid(column=0,row=2,sticky=(W))
       ttk.Button(mainFrame,text="Cancelar",command=self.cerrar).grid(column=0,row=2,pady=20,sticky=(W),padx=100)
       ttk.Button(mainFrame,text="Lista",command=self.lista1).grid(column=0,row=2,pady=20,padx=200,sticky=(W))
       ttk.Button(mainFrame,text="ddb",command= self.bdd).grid(column=0, row=2, padx=300,pady=20,sticky=(W))
       

       ttk.Radiobutton(mainFrame4,text="Estudiante",variable=self.ocupacion,value="Estudiante").grid(column=0,row=0,sticky=(W),padx=30)
       ttk.Radiobutton(mainFrame4,text="Empleado",variable=self.ocupacion,value="Empleado").grid(column=0,row=1,sticky=(W),padx=30)
       ttk.Radiobutton(mainFrame4,text="Desempleado",variable=self.ocupacion,value="Desempleado").grid(column=0,row=2,sticky=(W),padx=30)

       comboboxestados = ttk.Combobox(mainFrame,textvariable=self.estado)
       comboboxestados.grid(column=1,row=1)
       comboboxestados['values'] = ("Aguascalientes",
                            "Baja California","Baja California Sur", "Campeche","Coahuila",
                            "Colima","Chiapas","Chihuahua","Durango","Distrito Federal","Guanajuato",
                            "Guerrero","Hidalgo","Jalisco","México","Michoacán","Morelos", "Nayarit", 
                            "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", 
                            "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", 
                            "Zacatecas")
       self.raiz.mainloop()
    def lista1(self):
        cuadro = Toplevel(self.raiz)
        cuadro.title("Datos almacenados")
        
        with open("lista.csv", mode="r") as archivo:
            leer = csv.reader(archivo)

           
            tableframe = ttk.LabelFrame(cuadro, text='lista')
            tableframe.pack(fill=BOTH, expand=1, padx=5, pady=5)

            num = 0
            for row in leer:
                label = ttk.Label(tableframe, text=row[0], width=20, borderwidth=1, relief='solid')
                label.grid(row=num, column=0)
                
                label2 = ttk.Label(tableframe, text=row[1], width=20, borderwidth=1, relief='solid')
                label2.grid(row=num, column=1)
                
                label3 = ttk.Label(tableframe, text=row[2], width=20, borderwidth=1, relief='solid')
                label3.grid(row=num, column=2)

                label4 = ttk.Label(tableframe, text=row[3], width=20, borderwidth=1, relief='solid')
                label4.grid(row=num, column=3)
                
                label5 = ttk.Label(tableframe, text=row[4], width=20, borderwidth=1, relief='solid')
                label5.grid(row=num, column=4)
                
                label6 = ttk.Label(tableframe, text=row[5], width=20, borderwidth=1, relief='solid')
                label6.grid(row=num, column=5)

                label7 = ttk.Label(tableframe, text=row[6], width=20, borderwidth=1, relief='solid')
                label7.grid(row=num, column=6)
                
                label8 = ttk.Label(tableframe, text=row[7], width=20, borderwidth=1, relief='solid')
                label8.grid(row=num, column=7)
                
                label9 = ttk.Label(tableframe, text=row[8], width=20, borderwidth=1, relief='solid')
                label9.grid(row=num, column=8)

                label10 = ttk.Label(tableframe, text=row[9], width=20, borderwidth=1, relief='solid')
                label10.grid(row=num, column=9)

                num += 1
                   
    def guardarLista(self):
    
            nombre_ = self.Nombre.get()
            APaterno_ = self.APaterno.get()
            AMaterno_ = self.AMaterno.get()
            Correo_ = self.Correo.get() 
            Movil_ = self.movil.get()
            Aficion = self.aficion.get()
            Aficion2 = self.aficionn.get()
            Aficion3 = self.aaficion.get()
            Estado1 = self.estado.get()
            Ocupacion = self.ocupacion.get()

            with open("lista.csv", mode="a", newline="") as archivo:

                escritor = csv.writer(archivo)
            
                if archivo.tell() == 0:
                    escritor.writerow(['Nombre','Apaterno','Amaterno','Correo','Movil','Leer','Musica','Videojuegos','Estado','Ocupacion'])
           
                escritor.writerow([nombre_, APaterno_, AMaterno_, Correo_, Movil_, Aficion, Aficion2, Aficion3, Estado1, Ocupacion])
        
        
            self.Nombre.delete(0,"end")
            self.APaterno.delete(0,"end")
            self.AMaterno.delete(0,"end")
            self.Correo.delete(0,"end")
            self.movil.delete(0,"end")
            self.aficion.set(False)
            self.aficionn.set(False)
            self.aaficion.set(False)
            self.estado.set("Estados")
            self.ocupacion.set("")

    def cerrar(self):
        self.raiz.destroy()



    def bdd (self):
            
            conexion = sqlite3.connect('lista.db')
            c= conexion.cursor()

            nombrebdd = self.Nombre.get()
            paternobdd = self.APaterno.get()
            maternobdd = self.AMaterno.get() 
            correobdd = self.Correo.get()
            movilbdd = self.movil.get()
            leerbdd = self.leer.get()
            musicabdd=self.musica.get()
            videojuegosbdd =self.videojuegos.get()
            estudiantebdd = self.estudiante.get()
            empleadobdd = self.empleado.get()
            desempleadobdd = self.desempleado.get()
            estadobdd = self.estado.get()
   
            self.Nombre.delete(0,"end")
            self.APaterno.delete(0,"end")
            self.AMaterno.delete(0,"end")
            self.Correo.delete(0,"end")
            self.movil.delete(0,"end")

            self.leer.set(False)
            self.musica.set(False)
            self.videojuegos.set(False)
            self.estudiante.set(False)
            self.empleado.set(False)
            self.desempleado.set(False)
            self.estado.set("Estados")
                 
            lista =[(nombrebdd, paternobdd, maternobdd, correobdd, movilbdd, leerbdd, musicabdd, videojuegosbdd, estudiantebdd, empleadobdd, desempleadobdd, estadobdd)]

            c.executemany('INSERT INTO Lista1 VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',lista)
            conexion.commit()
            conexion.close()    


    

Fuente()