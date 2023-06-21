from communication.client.client import MountainClient
from escalador import Escalador
import math
import time
pi = math.pi

    
def find_entry_with_cima(data):
    for territory, territory_values in data.items():
        for entry, entry_values in territory_values.items():
            if entry_values.get('cima', False):
                return entry
    return False
def list_with_z (data ,escaladoor):
    respuesta = []
    for equipo in data :
        for escladores in data[equipo]:
            if escladores != escalador:
                respuesta.append(data[equipo][escladores]['z'])
    return respuesta
#c= MountainClient('10.42.0.1',8888)
c=MountainClient()
c.add_team('T1', ['E1','E2','E3','E4'])
E1=Escalador("E1",1)
E2=Escalador("E2",2)
E3=Escalador("E3",3)
E4=Escalador("E4",4)
c.finish_registration()
cuadrante_division=False
while not c.is_over():
    speed = 50
    lista_escaladores = [E1, E2, E3, E4]
    direccion = {}
    data = c.get_data()
    #print(data)
    cima=find_entry_with_cima(data)
    time.sleep(0)
    if cima== False:
            for escalador in lista_escaladores:
                 z_escladores= list_with_z(data,escalador.nombre)
                 direccion[escalador.nombre] = {'direction': escalador.calculate_direction(data['T1'][escalador.nombre]['inclinacion_x'],
                                                data['T1'][escalador.nombre]['inclinacion_y'],
                                                data['T1'][escalador.nombre]['x'],
                                                data['T1'][escalador.nombre]['y'],
                                                data['T1'][escalador.nombre]['z'],
                                                z_escladores),
                                                'speed' : speed} 
    else:

        for escalador in lista_escaladores:
            if escalador.nombre ==cima:
                direccion[escalador.nombre] = {'direction': escalador.calculate_direction(data['T1'][escalador.nombre]['inclinacion_x'],
                                                data['T1'][escalador.nombre]['inclinacion_y'],
                                                data['T1'][escalador.nombre]['x'],
                                                data['T1'][escalador.nombre]['y'],
                                                data['T1'][escalador.nombre]['z'],
                                                z_escladores),
                                                'speed' : speed} 
            else:
                direccion[escalador.nombre] = {'direction': escalador.calcular_angulo(
                                                                                data['T1'][escalador.nombre]['x'],
                                                                                data['T1'][escalador.nombre]['y'],
                                                                                data['T1'][cima]['x'],
                                                                                data['T1'][cima]['y']
                                                                               ),
                                                                               'speed' : speed} 
                print("Se encontro la cima ", direccion)
    c.next_iteration('T1',direccion)