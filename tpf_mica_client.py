from communication.client.client import MountainClient
from tpf_mica_escalador import Escalador
import math
import time
import socket
pi = math.pi

import argparse

# Crear el parser de argumentos
parser = argparse.ArgumentParser()

# Agregar un argumento "--ip" al parser
parser.add_argument("--ip", help="Dirección IP y puerto")

# Obtener los argumentos de la línea de comandos
args = parser.parse_args()

# Acceder al valor del argumento "--ip"
ip = args.ip

# Imprimir el valor del argumento "--ip"
while True:
    if ip is None:
        print("No direccion IP  ni puerto dados. Default localhost:8080")
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

def encontrar_entrada_con_cima(data: dict) -> tuple:
    """
    Encuentra la entrada con el valor 'cima' establecido en True en los datos proporcionados.

    Args:
        data (dict): Datos que contienen territorios y entradas.

    Returns:
        tuple: Una tupla con el equipo y el escalador de la entrada que tiene 'cima' como True. Si no se encuentra ninguna entrada con 'cima' como True, se devuelve (None, None).
    """
    for territorio, valores_territorio in data.items():
        for entrada, valores_entrada in valores_territorio.items():
            if valores_entrada.get('cima', False):
                return (territorio, entrada)
    return (None, None)
def top_z_checker (data:dict , top_Z:list)->float:
    """
    Chequea todos los z de los equipos y devuelve el mas grande a lo largo del tiempo

    Args:
        data (dict): Datos que contienen territorios y entradas.
        top_Z (float): z mas grande.

    Returns:
        El z mas grande de esa iteracion.
    """
    respuesta_escalador= top_Z[0]
    respuesta_z = top_Z[1]

    for equipo in data:
        for escalador in data[equipo]:
            posible_z = data[equipo][escalador]['z']
            if posible_z>respuesta_z:
                respuesta_escalador=escalador
                respuesta_z =  posible_z
    return respuesta_escalador, respuesta_z

# ...

while True:
    try:
        c = MountainClient(ip,int(port))

        # Agregar equipos y escaladores
        c.add_team('MICA', ['ISA', 'BRUNO', 'ESTANISLAO', 'CAMILA'])

        break  # Si la conexión es exitosa, salimos del bucle

    except (ConnectionRefusedError, socket.gaierror,OSError):
        print("No se pudo establecer una conexión con el servidor. Asegúrate de que el servidor esté en funcionamiento y el puerto sea correcto.")
        print("IP y puerto proporcionados: ", ip, ":", port)

        while True:
            opcion = input("¿Qué deseas hacer?\n1. Volver a intentar la conexión con el mismo IP:puerto\n2. Ingresar otro IP:puerto\n3. Salir del programa\nOpción: ")

            if opcion == "1":
                break  # Salir del bucle interno y volver a intentar la conexión con el mismo IP:puerto
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

                    break  # Salir del bucle interno y continuar con el siguiente paso

                break  # Salir del bucle interno y continuar con el siguiente paso
            elif opcion == "3":
                print("Saliendo del programa.")
                exit()  # Salir del programa
            else:
                print("Opción inválida. Por favor, elige una opción válida.")


# Agregar equipos y escaladores

c.add_team('MICA', ['ISA', 'BRUNO', 'ESTANISLAO', 'CAMILA'])
ISA = Escalador("ISA", 1)
BRUNO = Escalador("BRUNO", 2)
ESTANISLAO = Escalador("ESTANISLAO", 3)
CAMILA = Escalador("CAMILA", 4)

top_z =["",0]
while not c.is_over():
    velocidad = 50
    lista_escaladores = [ISA, BRUNO, ESTANISLAO, CAMILA]
    direccion = {}
    data = c.get_data()
    #print(data)
    #time.sleep(0.3)
    team, hiker = encontrar_entrada_con_cima(data)
    top_z[0] , top_z[1] = top_z_checker(data,top_z)
    if hiker is None:
        for escalador in lista_escaladores:
            if escalador.nombre in data['MICA']:
                direccion[escalador.nombre] = {
                    'direction': escalador.calcular_direccion(
                    data['MICA'][escalador.nombre]['inclinacion_x'],
                    data['MICA'][escalador.nombre]['inclinacion_y'],
                    data['MICA'][escalador.nombre]['x'],
                    data['MICA'][escalador.nombre]['y']
                    ),
                'speed': velocidad}
    else:
        for escalador in lista_escaladores:
         if escalador.nombre in data['MICA']:
            if escalador.nombre == hiker and  team == 'MICA':
                direccion[escalador.nombre] = {
                    'direction': escalador.calcular_direccion(
                        data['MICA'][escalador.nombre]['inclinacion_x'],
                        data['MICA'][escalador.nombre]['inclinacion_y'],
                        data['MICA'][escalador.nombre]['x'],
                        data['MICA'][escalador.nombre]['y']),
                    'speed': velocidad}
            else:
                direccion[escalador.nombre] = {
                    'direction': escalador.calcular_angulo(
                        data['MICA'][escalador.nombre]['x'],
                        data['MICA'][escalador.nombre]['y'],
                        data[team][hiker]['x'],
                        data[team][hiker]['y']
                    ),
                    'speed': velocidad}

    c.next_iteration('MICA', direccion)
