from communication.client.client import MountainClient
import math
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
c= MountainClient()
c.add_team('T1', ['E1','E2','E3','E4'])
E1=Escalador("E1",1)
E2=Escalador("E2",2)
E3=Escalador("E3",3)
E4=Escalador("E4",4)
c.finish_registration()
cuadrante_division=False
while not c.is_over():
    data = c.get_data()
    print(data)
    speed = 50
    direccionE1= E1.calculate_direction(data['T1'][E1.nombre]['inclinacion_x'],data['T1'][E1.nombre]['inclinacion_y'],data['T1'][E1.nombre]['x'], data['T1'][E1.nombre]['y'])
    direccionE2= E2.calculate_direction(data['T1'][E2.nombre]['inclinacion_x'],data['T1'][E2.nombre]['inclinacion_y'],data['T1'][E2.nombre]['x'], data['T1'][E2.nombre]['y'])
    direccionE3= E3.calculate_direction(data['T1'][E3.nombre]['inclinacion_x'],data['T1'][E3.nombre]['inclinacion_y'],data['T1'][E3.nombre]['x'], data['T1'][E3.nombre]['y'])
    direccionE4= E4.calculate_direction(data['T1'][E4.nombre]['inclinacion_x'],data['T1'][E4.nombre]['inclinacion_y'],data['T1'][E4.nombre]['x'], data['T1'][E4.nombre]['y'])
    print(direccionE1)
    c.next_iteration('T1',{E1.nombre:{'direction':direccionE1,'speed':speed},
                           E2.nombre:{'direction':direccionE2,'speed':speed},
                           E3.nombre:{'direction':direccionE3,'speed':speed},
                           E4.nombre:{'direction':direccionE4,'speed':speed}})
