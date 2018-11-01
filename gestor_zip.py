import zipfile
import subprocess

while True:
    archiv_zip=input("Introduce archivo zip: ")
    
    with zipfile.ZipFile(archiv_zip, 'w') as archivo_zip:
        for i in range(4):
            archo=input("Introduzca archivo a ingresar: ")
            archivo_zip.write(archo)

    conti=input("¿Desea continuar?: ")
    while conti!="n" and conti!="s":
        conti=input("Escriba solo \'n\' o \'s\' según su opción: ")

    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
