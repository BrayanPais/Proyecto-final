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
                    elif hora_actual_dt > hora_entrada_dt + timedelta(hours=7, minutes=30):
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
def asistencia():
    nombre=entrada1.get()
    no_trabajo=int(entrada2.get())
    nombre_minusculas=nombre.lower()
    hora_entrada=time(empresa[f"{nombre_minusculas}"]["Hora entrada"],0,0)
    persona1=persona(nombre_minusculas,no_trabajo,hora_entrada)
    persona1.tomar_asistencia()    
ventana = tk.Tk()
ventana.title("Sistema de asistencias")
empresa={
 "rivelino":{"Nombre":"rivelino",
  "Edad":30,
  "N°.trabajador":123456,
  "Hora entrada":7,
  "Hora salida":14,
  "Minutos salida":30,
  "Asistencias totales":0,
  "Retardos menores":0,
  "Retardos mayores":0,
  "Faltas":0}
}
label1 = tk.Label(ventana, text="Ingresa tu nombre:")
label1.grid(row=0, column=0, padx=5, pady=5)  
entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=1, padx=5, pady=5)  
label2 = tk.Label(ventana, text="Ingresa tu N° de trabajador:")
label2.grid(row=1, column=0, padx=5, pady=5)  
entrada2 = tk.Entry(ventana)
entrada2.grid(row=1, column=1, padx=5, pady=5)
label3 = tk.Label(ventana, text="Ingresa tu ocupacion")
label3.grid(row=2, column=0, padx=5, pady=5)
entrada3 = tk.Entry(ventana)
entrada3.grid(row=2, column=1, padx=5, pady=5)  
sumar_btn = tk.Button(ventana, text="Tomar asistencia", command=asistencia)  
sumar_btn.grid(row=3, column=0, columnspan=2, pady=10)  
resultado_label = tk.Label(ventana, text="")
resultado_label.grid(row=4, column=0, columnspan=2, pady=5)
ventana.mainloop()
