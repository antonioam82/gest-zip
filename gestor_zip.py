import zipfile
import subprocess
import os

lista_ar=os.listdir()

while True:
    print("Introduzca la acción a ejecutar")
    print("A)AÑADIR ELEMENTOS A UN ZIP")
    print("B)VER ELEMENTOS CONTENIDO EN UN ZIP")
    print("C)VER CONTENIDO DE UN ELEMENTO")
    print("D)EXTRAER UN ZIP")
    op=input("Introduzca aquí su opción: ")
    while op!="A" and op!="B" and op!="C" and op!="D":
        op=input("Introduzca solo \'A\', \'B\', \'C\' o \'D\' seg,un su opción: ")
        
    if op=="A":
        archiv_zip=input("Introduzca archivo zip: ")
        archivos=input("introduzca los archivos a insertar separados por coma: ")
        lista_archivos=list(archivos.split(","))
        with zipfile.ZipFile(archiv_zip,'w') as archivo_zip:
            for i in lista_archivos:
                if not i in lista_ar:
                    print("No se encontró el archivo",i)
                    continue
                archivo_zip.write(i)
    if op=="B":
        archiv_zip=input("Introduzca archivo zip: ")
        if not archiv_zip in lista_ar:
            print("Carpeta no encontrada")
            continue
        with zipfile.ZipFile(archiv_zip,'r') as archivo_zip:
            list_files=archivo_zip.namelist()
            print(list_files)
    if op=="C":
        archiv_zip=input("Introduzca archivo zip: ")
        if not archiv_zip in lista_ar:
            print("Carpeta no encontrada")
            continue
        archi=input("Introduzca el archivo que desea ver: ")
        if not archi in archiv_zip:
            print("Archivo no encontrado")
            continue
        with zipfile.ZipFile(archiv_zip,'r') as archivo_zip:
            with archivo_zip.open(archi,'r') as texto:
                print(texto.read())
    if op=="D":
        archiv_zip=input("Introduzca archivo zip: ")
        if not archiv_zip in lista_ar:
            print("Carpeta no encontrada")
            continue
        with zipfile.ZipFile(archiv_zip,'r') as archivo_zip:
            archivo_zip.extractall(pwd=None)
    archivo_zip.close()
    lista_ar=os.listdir(-Path-)
        

    conti=input("¿Desea continuar?: ")
    while conti!="n" and conti!="s":
        conti=input("Escriba solo \'n\' o \'s\' según su opción: ")

    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
            
        
