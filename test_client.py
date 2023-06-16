from communication.client.client import MountainClient
import math
import time
pi = math.pi
class Escalador :
    def __init__(self,nombre,cuadrante) -> None:
        self.nombre = nombre
        self.cuadrante=cuadrante 
        self.maximo =0
        self.in_cuadrante=False
    
    def is_incuadrante(self, posicion_x , posicion_y):
        if self.cuadrante==1 and posicion_x>=14000 and posicion_y>=14000:
            self.in_cuadrante=True
        elif self.cuadrante==2 and posicion_x<=-14000 and posicion_y>=14000:
            self.in_cuadrante=True
        elif self.cuadrante==3 and posicion_x<=-14000 and posicion_y<=-14000:
            self.in_cuadrante=True
        elif self.cuadrante==4 and posicion_x>=14000 and posicion_y<=-14000:
            self.in_cuadrante=True
    
    def calculate_direction(self, inclinacion_x, inclinacion_y, posicion_x , posicion_y):
        self.is_incuadrante(posicion_x, posicion_y)
        if self.in_cuadrante:
            return self.inclinacion(inclinacion_x, inclinacion_y)
        else:
            return self.go_cuadrante()
        

    def inclinacion(self,inclinacion_x, inclinacion_y):
        if inclinacion_x>0 and inclinacion_y>0:
        #Cuadrante 1
            diferencia= inclinacion_y-inclinacion_x
            if diferencia >0:
                porcentaje=  diferencia/inclinacion_x
                direction= (pi/4)+(pi/4 )* (min(porcentaje,1))
            else:
                porcentaje= abs(diferencia)/inclinacion_y
                direction = pi/4 -(pi/4)*(min(porcentaje,1))
        elif inclinacion_x<0 and inclinacion_y>0:
        #Cuadrante 2
            diferencia = inclinacion_y - abs(inclinacion_x)
            if diferencia>0:
                porcentaje= diferencia/abs(inclinacion_x)
                direction= (3*pi/4)-(pi/4*(min(porcentaje,1)))
            else:
                porcentaje= abs(diferencia)/inclinacion_y
                direction = (3*pi/4)+(pi/4*(min(porcentaje,1)))
        elif inclinacion_x<0 and inclinacion_y<0:
        #Cuadrante 3
            diferencia = abs(inclinacion_y) - abs(inclinacion_x)
            if diferencia>0:
                porcentaje= diferencia/abs(inclinacion_x)
                direction= (5*pi/4)+(pi/4*(min(porcentaje,1)))
            else:
                porcentaje= abs(diferencia)/abs(inclinacion_y)
                direction = (5*pi/4)-(pi/4*(min(porcentaje,1)))   
        elif inclinacion_x>0 and inclinacion_y<0:
        #Cuadrante 4
            diferencia = abs(inclinacion_y) - inclinacion_x
            if diferencia>0:
                porcentaje= diferencia/inclinacion_x
                direction= (7*pi/4)-(pi/4*(min(porcentaje,1)))
            else:
                porcentaje= abs(diferencia)/abs(inclinacion_y)
                direction = (7*pi/4)+(pi/4*(min(porcentaje,1)))          
        return direction
    
    
    def set_maximo(self,valor):
        if self.maximo < valor:
            self.maximo = valor


    def __lt__(self,other):
        if self.maximo < other.maximo:
            return self.get_to_center()
    def get_to_center(self):
        if self.cuadrante==1:
            return 5*pi/4
        if self.cuadrante==2:
            return 7*pi/4
        if self.cuadrante==3:
          return  pi/4
        if self.cuadrante==4:
            return 3*pi/4
    def go_cuadrante (self):
        if self.cuadrante==2:
            return pi
        if self.cuadrante==3:
            return 5*pi/4
        if self.cuadrante==4:
            return 6*pi/4
    def seguir_A(self,posicion_x_A, posicion_x_B, posicion_y_A, posicion_y_B):
        if posicion_y_B < posicion_y_A:
            if posicion_x_B > posicion_x_A:
                return pi + math.atan((posicion_y_B-posicion_y_A)/(posicion_x_B-posicion_x_A))
            else:
               return math.atan((posicion_y_B-posicion_y_A)/(posicion_x_B-posicion_x_A))
        else:
            if posicion_x_B > posicion_x_A:
                return pi + math.atan((posicion_y_B-posicion_y_A)/(posicion_x_B-posicion_x_A))
            else:
               return 2*pi + math.atan((posicion_y_B-posicion_y_A)/(posicion_x_B-posicion_x_A))
    def calcular_angulo(self,posicion_x_A, posicion_x_B, posicion_y_A, posicion_y_B):
        dx = posicion_x_A - posicion_x_B
        dy = posicion_y_A - posicion_y_B
        angulo_radianes = math.atan2(dy, dx)
        angulo_ajustado = math.fmod(angulo_radianes, (2*math.pi))
        if angulo_ajustado < 0:
            angulo_ajustado += 2*math.pi
        return angulo_ajustado
    def linea_de_fuego(self, posicon_x, posicion_y):
        if posicon_x or posicion_y >= 22800:
            pass
    
def find_entry_with_cima(data):
    for territory, territory_values in data.items():
        for entry, entry_values in territory_values.items():
            if entry_values.get('cima', False):
                return entry
    return False
        
c= MountainClient()
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
    print(data)
    cima=find_entry_with_cima(data)
    if cima== False:
            for escalador in lista_escaladores:
                 direccion[escalador.nombre] = {'direction': escalador.calculate_direction(data['T1'][escalador.nombre]['inclinacion_x'],
                                                data['T1'][escalador.nombre]['inclinacion_y'],
                                                data['T1'][escalador.nombre]['x'],
                                                data['T1'][escalador.nombre]['y']),
                                                'speed' : speed} 
    else:

        for escalador in lista_escaladores:
            if escalador.nombre ==cima:
                direccion[escalador.nombre] = {'direction': escalador.calculate_direction(data['T1'][escalador.nombre]['inclinacion_x'],
                                                data['T1'][escalador.nombre]['inclinacion_y'],
                                                data['T1'][escalador.nombre]['x'],
                                                data['T1'][escalador.nombre]['y']),
                                                'speed' : speed} 
            else:
                direccion[escalador.nombre] = {'direction': escalador.seguir_A(data['T1'][cima]['x'],
                                                                               data['T1'][escalador.nombre]['x'],
                                                                               data['T1'][cima]['y'],
                                                                               data['T1'][escalador.nombre]['y']),
                                                                               'speed' : speed} 
    time.sleep(0)
    c.next_iteration('T1',direccion)