from communication.client.client import MountainClient
from escalador import Escalador
import math
import time
pi = math.pi

def encontrar_entrada_con_cima(data: dict) -> bool:
    """
    Encuentra la entrada con el valor 'cima' establecido en True en los datos proporcionados.

    Args:
        data (dict): Datos que contienen territorios y entradas.

    Returns:
        bool: True si se encuentra una entrada con el valor 'cima', False de lo contrario.
    """
    for territorio, valores_territorio in data.items():
        for entrada, valores_entrada in valores_territorio.items():
            if valores_entrada.get('cima', False):
                return entrada
    return False


def lista_con_z(data: dict, escalador: str) -> list:
    """
    Crea una lista de valores 'z' para todos los escaladores excepto el especificado.

    Args:
        data (dict): Datos que contienen territorios y entradas.
        escalador (str): Nombre del escalador.

    Returns:
        list: Lista de valores 'z' para los demás escaladores.
    """
    respuesta = []
    for equipo in data:
        for escaladores in data[equipo]:
            if escaladores != escalador:
                respuesta.append(data[equipo][escaladores]['z'])
    return respuesta


c = MountainClient()

# Agregar equipos y escaladores

c.add_team('T1', ['E1', 'E2', 'E3', 'E4'])
E1 = Escalador("E1", 1)
E2 = Escalador("E2", 2)
E3 = Escalador("E3", 3)
E4 = Escalador("E4", 4)

c.finish_registration()

while not c.is_over():
    velocidad = 50
    lista_escaladores = [E1, E2, E3, E4]
    direccion = {}
    data = c.get_data()
    cima = encontrar_entrada_con_cima(data)
    time.sleep(0)

    if cima is False:
        for escalador in lista_escaladores:
            z_escaladores = lista_con_z(data, escalador.nombre)
            direccion[escalador.nombre] = {
                'direction': escalador.calcular_direccion(
                    data['T1'][escalador.nombre]['inclinacion_x'],
                    data['T1'][escalador.nombre]['inclinacion_y'],
                    data['T1'][escalador.nombre]['x'],
                    data['T1'][escalador.nombre]['y'],
                    data['T1'][escalador.nombre]['z'],
                    z_escaladores),
                'speed': velocidad}
    else:
        for escalador in lista_escaladores:
            if escalador.nombre == cima:
                direccion[escalador.nombre] = {
                    'direction': escalador.calcular_direccion(
                        data['T1'][escalador.nombre]['inclinacion_x'],
                        data['T1'][escalador.nombre]['inclinacion_y'],
                        data['T1'][escalador.nombre]['x'],
                        data['T1'][escalador.nombre]['y'],
                        data['T1'][escalador.nombre]['z'],
                        z_escaladores),
                    'speed': velocidad}
            else:
                direccion[escalador.nombre] = {
                    'direction': escalador.calcular_angulo(
                        data['T1'][escalador.nombre]['x'],
                        data['T1'][escalador.nombre]['y'],
                        data['T1'][cima]['x'],
                        data['T1'][cima]['y']
                    ),
                    'speed': velocidad}
        print("Se encontró la cima", direccion)

    c.next_iteration('T1', direccion)
