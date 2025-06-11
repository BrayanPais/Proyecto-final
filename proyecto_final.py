import tkinter as tk
from datetime import datetime, time, timedelta
class persona():
    def __init__(self,nombre,no_trabajo,hora_entrada):
        self.nombre=nombre
        self.no_trabajo=no_trabajo
        self.hora_entrada=hora_entrada
    def tomar_asistencia(self):
        hora_actual=datetime.now().time()
        nombre_registrado=empresa[f"{self.nombre}"]["Nombre"]
        no_trabajo_registrado=empresa[f"{self.nombre}"]["N°.trabajador"]
        hora_actual_dt = datetime.combine(datetime.today(), hora_actual)
        hora_entrada_dt = datetime.combine(datetime.today(), self.hora_entrada)
        if self.nombre==nombre_registrado:
            if self.no_trabajo==no_trabajo_registrado:
                if hora_actual_dt > hora_entrada_dt:
                    if hora_actual_dt > hora_entrada_dt + timedelta(minutes=10) and hora_actual_dt < hora_entrada_dt + timedelta(hours=7, minutes=30):
                        empresa[f"{self.nombre}"]["Retardos mayores"]+=1
                        resultado_label.config(text="Se ha tomado asistencia con una falta mayor")
                        if empresa[f"{self.nombre}"]["Retardos mayores"]==2:
                            empresa[f"{self.nombre}"]["Faltas"]+=1
                            empresa[f"{self.nombre}"]["Retardos mayores"]=0
                        with open ("Asistencia_de_trabajadores.txt","a") as archivo:
                            archivo.write(f"{self.nombre} ha tomado asistencia con una falta mayor\n")
                    elif hora_actual_dt > hora_entrada_dt + timedelta(hours=8, minutes=30):
                        empresa[f"{self.nombre}"]["Faltas"]+=1
                        resultado_label.config(text="Se ha tomado una falta")
                        with open ("Asistencia_de_trabajadores.txt","a") as archivo:
                            archivo.write(f"{self.nombre} ha faltado\n")
                    else:
                        empresa[f"{self.nombre}"]["Retardos menores"]+=1
                        resultado_label.config(text="Se ha tomado asistencia con una falta menor")
                        if empresa[f"{self.nombre}"]["Retardos menores"]==3:
                            empresa[f"{self.nombre}"]["Faltas"]+=1
                            empresa[f"{self.nombre}"]["Retardos menores"]=0
                            with open ("Asistencia_de_trabajadores.txt","a") as archivo:
                                archivo.write(f"{self.nombre} ha tomado asistencia con una falta menor\n")
                else:
                    empresa[f"{self.nombre}"]["Asistencias totales"]+=1
                    resultado_label.config(text="Se ha tomado asistencia correctamente")
                    with open ("Asistencia_de_trabajadores.txt","a") as archivo:
                        archivo.write(f"{self.nombre} ha tomado asistencia\n")
            else:
                resultado_label.config(text="El numero de trabajador no esta registrado")    
        else:
            resultado_label.config(text="El nombre ingresado no esta registrado")
def interfas_uno():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Toma de asistencia", font=("Arial", 14)).pack(pady=10)
    label1 = tk.Label(area_dinamica, text="Ingresa tu nombre:")
    label1.pack(pady=5)  
    entrada1 = tk.Entry(area_dinamica)
    entrada1.pack(pady=5)  
    label2 = tk.Label(area_dinamica, text="Ingresa tu N° de trabajador:")
    label2.pack(pady=5)  
    entrada2 = tk.Entry(area_dinamica)
    entrada2.pack(pady=5)
    label3 = tk.Label(area_dinamica, text="Ingresa tu ocupacion:")
    label3.pack(pady=5)
    entrada3 = tk.Entry(area_dinamica)
    entrada3.pack(pady=5)  
    sumar_btn = tk.Button(area_dinamica, text="Tomar asistencia", command=asistencia)
    sumar_btn.pack(pady=5)
    resultado_label = tk.Label(area_dinamica, text="")
    resultado_label.pack(pady=5)
def interfas_dos():
    area_dinamica_limpia()
    global a
    a=1
def comprobar_contraseña():
    contraseña=int(entrada1.get())
    if contraseña==1113420:
        if a==1:
            interfas_dos()
        elif a==2:
            pass
        else:
            pass
    else:
        if a==1:
            pass
        elif a==2:
            pass
        else:
            pass
def asistencia():
    nombre=entrada1.get()
    no_trabajo=int(entrada2.get())
    nombre_minusculas=nombre.lower()
    if empresa[f"{nombre_minusculas}"]["Turno"]=="Matutino":
        hora_entrada=time(7,0,0)
    elif empresa[f"{nombre_minusculas}"]["Turno"]=="Vespertino":
        hora_entrada=time(15,0,0)
    elif empresa[f"{nombre_minusculas}"]["Turno"]=="Nocturno":
        hora_entrada=time(23,0,0)        
    persona1=persona(nombre_minusculas,no_trabajo,hora_entrada)
    persona1.tomar_asistencia()
def area_dinamica_limpia():
    for widget in area_dinamica.winfo_children():
        widget.destroy()
ventana = tk.Tk()
ventana.title("Sistema de asistencias")
ventana.geometry("500x400")
empresa={
    "rivelino":{"Nombre":"rivelino","Edad":30,"N°.trabajador":123456,"Turno":"Matutino","Asistencias totales":0,"Retardos menores":0,"Retardos mayores":0,"Faltas":0},
    "oscar":{"Nombre":"oscar","Edad":31,"N°.trabajador":654321,"Turno":"Vespertino","Asistencias totales":0,"Retardos menores":0,"Retardos mayores":0,"Faltas":0},
    "ashley":{"Nombre":"ashley","Edad":20,"N°.trabajador":987654,"Turno":"Nocturno","Asistencias totales":0,"Retardos menores":0,"Retardos mayores":0,"Faltas":0}
}
menu_lateral = tk.Frame(ventana, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")
area_dinamica = tk.Frame(ventana, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")
tk.Button(menu_lateral, text="Tomar asistencia",command=interfas_uno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Agregar registro",command=interfas_dos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Cambiar registro", width=15).pack(pady=10)
tk.Button(menu_lateral, text="Eliminar registro", width=15).pack(pady=10)
tk.Label(area_dinamica, text="Toma de asistencia", font=("Arial", 14)).pack(pady=10)
label1 = tk.Label(area_dinamica, text="Ingresa tu nombre:")
label1.pack(pady=5)
entrada1 = tk.Entry(area_dinamica)
entrada1.pack(pady=5)
label2 = tk.Label(area_dinamica, text="Ingresa tu N° de trabajador:")
label2.pack(pady=5)
entrada2 = tk.Entry(area_dinamica)
entrada2.pack(pady=5)
label3 = tk.Label(area_dinamica, text="Ingresa tu ocupacion:")
label3.pack(pady=5)
entrada3 = tk.Entry(area_dinamica)
entrada3.pack(pady=5)
sumar_btn = tk.Button(area_dinamica, text="Tomar asistencia", command=asistencia)
sumar_btn.pack(pady=5)
resultado_label = tk.Label(area_dinamica, text="")
resultado_label.pack(pady=5)
ventana.mainloop()
