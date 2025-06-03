import tkinter as tk
from datetime import datetime, time, timedelta
def asistencia():
    nombre=entrada1.get()
    no_trabajo=int(entrada2.get())
    hora_entrada=time(7,0,0)
    hora_actual=datetime.now().time()
    nombre_registrado=rive_pers["Nombre"]
    no_trabajo_registrado=rive_pers["N°.trabajador"]
    hora_actual_dt = datetime.combine(datetime.today(), hora_actual)
    hora_entrada_dt = datetime.combine(datetime.today(), hora_entrada)
    if nombre==nombre_registrado:
        if no_trabajo==no_trabajo_registrado:
            if hora_actual_dt > hora_entrada_dt:
                if hora_actual_dt > hora_entrada_dt + timedelta(minutes=10):
                    rive_asis["Retardos mayores"]+=1
                    resultado_label.config(text="Se ha tomado asistencia con una falta mayor")
                    if rive_asis["Retardos mayores"]==2:
                        rive_asis["Faltas"]+=1
                        rive_asis["Retardos mayores"]=0
                else:
                    rive_asis["Retardos menores"]+=1
                    resultado_label.config(text="Se ha tomado asistencia con una falta menor")
                    if rive_asis["Retardos menores"]==3:
                        rive_asis["Faltas"]+=1
                        rive_asis["Retardos menores"]=0    
            else:
                rive_asis["Asistencias totales"]+=1
                resultado_label.config(text="Se ha tomado asistencia correctamente")
        else:
            resultado_label.config(text="El numero de trabajador no esta registrado")    
    else:
        resultado_label.config(text="El nombre ingresado no esta registrado")    
ventana = tk.Tk()
ventana.title("Sistema de asistencias")
rive_pers={"Nombre":"Rivelino",
 "Apellidos":"Reyes Gonzales",
 "Edad":30,
 "N°.trabajador":123456,
 "Sexo":"Hombre",
}
rive_asis={"Dias laborales":"L,M,V",
           "Hora entrada":"7,00",
           "Hora salida":"14:30",
           "Asistencias totales":0,
           "Retardos menores":0,
           "Retardos mayores":0,
           "Faltas":0}
label1 = tk.Label(ventana, text="Ingresa tu nombre:")
label1.grid(row=0, column=0, padx=5, pady=5)  
entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=1, padx=5, pady=5)  
label2 = tk.Label(ventana, text="Ingresa tu N° de trabajador:")
label2.grid(row=1, column=0, padx=5, pady=5)  
entrada2 = tk.Entry(ventana)
entrada2.grid(row=1, column=1, padx=5, pady=5)  
sumar_btn = tk.Button(ventana, text="Tomar asistencia", command=asistencia)  
sumar_btn.grid(row=2, column=0, columnspan=2, pady=10)  
resultado_label = tk.Label(ventana, text="")
resultado_label.grid(row=3, column=0, columnspan=2, pady=5)
ventana.mainloop()
