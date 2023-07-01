from communication.server.server import MountainServer
from communication.server.mountain.easy_mountain import EasyMountain
from communication.server.mountain.mccormick_mountain import McCormickMountain
from communication.server.mountain.mishra_mountain import MishraBirdMountain
from communication.server.mountain.ackley_mountain import AckleyMountain
from communication.server.mountain.easom_mountain import EasomMountain
from communication.server.mountain.rastrigin_mountain import RastriginMountain
from communication.server.mountain.sinosidal_mountain import SinosidalMountain 
import argparse
import socket

parser = argparse.ArgumentParser()

parser.add_argument("--ip", help="Dirección IP y puerto")

args = parser.parse_args()

# Acceder al valor del argumento "--ip"
ip = args.ip

# Imprimir el valor del argumento "--ip"
while True:
    if ip is None:
        print("No direccion IP  ni dados. Default localhost:8080")
        ip = "localhost:8080"
        ip, port = ip.split(":")
    else:
        print("La Ip y el Puerto dado son:", ip)
        ip_parts = ip.split(":")
        if len(ip_parts) != 2:
            print("Formato invalido. Por favor envielo 'ip:puerto'")
            ip = input("Escriba Ip:puerto: ")
            continue
        ip, port = ip_parts
        if not port.isdigit():
            print("Invalido numero de puerto. Por favor de un puerto valido")
            ip = input("Escriba Ip:puerto: ")
            continue
        port = int(port)
    break

# Solicitar la elección de la montaña al usuario
print("Elige una montaña para jugar:")
print("1. EasyMountain")
print("2. McCormickMountain")
print("3. MishraBirdMountain")
print("4. AckleyMountain")
print("5. EasomMountain")
print("6. RastriginMountain")
print("7. SinosidalMountain")

while True:
    eleccion = input("Enter the number corresponding to the mountain: ")
    if eleccion not in {"1", "2", "3", "4", "5", "6", "7"}:
        print("Invalid choice. Please enter a number between 1 and 7.")
    else:
        break

# Seleccionar la montaña según la elección del usuario
if eleccion == "1":
    mountain = EasyMountain(50, 23000)
elif eleccion == "2":
    mountain = McCormickMountain(50, 23000)
elif eleccion == "3":
    mountain = MishraBirdMountain(50, 23000)
elif eleccion == "4":
    mountain = AckleyMountain(50, 23000)
elif eleccion == "5":
    mountain = EasomMountain(50, 23000)
elif eleccion == "6":
    mountain = RastriginMountain(50, 23000)
elif eleccion == "7":
    mountain = SinosidalMountain(50, 23000)

# Crear el MountainServer con la montaña seleccionada y los parámetros proporcionados
s = MountainServer(mountain, (14000, 14000), 50, ip, int(port))
while True:
    try:
        s.start()
        break  # Si el servidor se inicia correctamente, salimos del bucle
    except (ConnectionRefusedError, socket.gaierror, OSError) as e:
        print("Failed to start the server:", str(e))
        print("IP y puerto proporcionados:", ip, ":", port)

        while True:
            opcion = input("¿Qué deseas hacer?\n1. Volver a intentar iniciar el servidor en el mismo IP:puerto\n2. Ingresar otro IP:puerto\n3. Salir del programa\nOpción: ")

            if opcion == "1":
                break  # Salir del bucle interno y volver a intentar iniciar el servidor en el mismo IP:puerto
            elif opcion == "2":
                while True:
                    ip_port = input("Ingrese otro IP:puerto (formato: IP:puerto): ")  # Pedir al usuario que ingrese otro IP:puerto

                    # Verificar el formato del IP:puerto ingresado
                    if ":" not in ip_port:
                        print("Formato incorrecto. Debe ingresar el IP y el puerto separados por ':'")
                        continue

                    ip, port = ip_port.split(":")  # Dividir el IP:puerto en IP y puerto

                    # Verificar que el puerto sea un número entero
                    if not port.isdigit():
                        print("El puerto debe ser un número entero.")
                        continue

                    break  

                break  
            elif opcion == "3":
                print("Saliendo del programa.")
                exit()  
            else:
                print("Opción inválida. Por favor, elige una opción válida.")
    