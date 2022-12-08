from os import system
import subprocess



if __name__=='__main__':
    while True:
        try:
            print("\t\t\t\t\t------------------------------------------------------")
            print("\t\t\t\t\t|Bienvenido a nuestra maquina de juegos Tradicionales|")
            print("\t\t\t\t\t------------------------------------------------------\n")
            opcion=-1
            print("\t\t\t\t\t1.-Telefono Descompuesto")
            print("\t\t\t\t\t2.-Escondidas")
            print("\t\t\t\t\t0.-Salir")
            opcion=int(input("\t\t\t\t\tIngrese el juego que desea jugar: "))
        except:
            print("No es ninguna opccion")
        if(opcion==1):
            subprocess.run('START "" "' + "[NRC_ 8001]_NicolasSuquillo_ProyectoUnidad1.py" + '"', shell=True)
            system("cls")
        elif (opcion==2):
            subprocess.run('START "" "' + "[NRC_8001]_AntoniToapanta_ProyectoUnidad1.py" + '"', shell=True)
            system("cls")
        elif (opcion==-1):
            system("cls")
            print("\t\t\t\t\tNo es una un numero!!!")
        elif opcion ==0:
            system("cls")
            break
        else:
            system("cls")
    system("pause")
