import zipfile
import subprocess

while True:
    archiv_zip=input("Introduce archivo zip: ")
    print("¿Qué acción quiere realizar?")
    print("A)CREAR ARCHIVO")
    print("B)VER ELEMENTOS DEL ARCHIVO")
    print("C)LEER UN ELEMENTO")
    print("D)EXTRAER ARCHIVO")
    op=input("Introduzca aquí su opción: ")
    while op!="A" and op!="B" and op!="C" and op!="D":
        op=input("Introduzca solo \'A\', \'B\', \'C\' o \'D\' según su opción: ")
        
    with zipfile.ZipFile(archiv_zip,'w')as archivo_zip:
        if op=="A":
            archo=input("introduzca archivo a ingresar: ")
            archivo_zip.write(archo)
        elif op=="B":
            list_files=archivo_zip.namelist()
            print(list_files)
        elif op=="C":
            archo=input("introduzca archivo a leer: ")
            with archivo_zip.open(archo,'r') as texto:
                print(texto.read())
        elif op=="D":
            archivo_zip.extractall(pwd=None)

    conti=input("¿Desea continuar?: ")
    while conti!="n" and conti!="s":
        conti=input("Escriba solo \'n\' o \'s\' según su opción: ")

    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
            
