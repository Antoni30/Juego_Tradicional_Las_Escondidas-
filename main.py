from os import system
import subprocess

try:
    opcion=-1
    print("1.-Telefono Descompuesto")
    print("2.-Escondidas")
    opcion=int(input("Ingrese el juego que desea jugar "))
except:
    print("No es ninguna opccion")
if(opcion==1):
    subprocess.run('START "" "' + "[NRC_ 8001]_NicolasSuquillo_ProyectoUnidad1.py" + '"', shell=True)
elif (opcion==2):
    subprocess.run('START "" "' + "[NRC_8001]_AntoniToapanta_ProyectoUnidad1.py" + '"', shell=True)
elif (opcion==-1):
    print("ninguna opcion")

system("pause")
