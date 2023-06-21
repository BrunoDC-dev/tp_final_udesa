
import math
pi = math.pi

def inclinacion(inclinacion_x, inclinacion_y):
    if inclinacion_x>0 and inclinacion_y>0:
        #Cuadrante 1
            diferencia= inclinacion_y-inclinacion_x
            if diferencia >0:
                direction= math.atan(inclinacion_y/inclinacion_x)
            else:
                direction = math.atan(inclinacion_y/inclinacion_x)
    elif inclinacion_x<0 and inclinacion_y>0:
        #Cuadrante 2
            diferencia = inclinacion_y - abs(inclinacion_x)
            if diferencia>0:
                direction= pi + math.atan(inclinacion_y/inclinacion_x)
            else:
                direction = pi + math.atan(inclinacion_y/inclinacion_x)
    elif inclinacion_x<0 and inclinacion_y<0:
        #Cuadrante 3
            diferencia = abs(inclinacion_y) - abs(inclinacion_x)
            if diferencia>0:
                direction= pi + math.atan(inclinacion_y/inclinacion_x)
            else:
                direction = pi + math.atan(inclinacion_y/inclinacion_x)   
    elif inclinacion_x>0 and inclinacion_y<0:
        #Cuadrante 4
            diferencia = abs(inclinacion_y) - inclinacion_x
            if diferencia>0:
                direction=((3*pi)/2 ) - math.atan(inclinacion_x/inclinacion_y)
            else:
                direction = 2*pi + math.atan(inclinacion_y/inclinacion_x)        
    return direction


def seguir_A(posicion_x_A, posicion_x_B, posicion_y_A, posicion_y_B):
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
print(seguir_A(0, 16,15, 0))

import math

import math

def calcular_angulo(xa, ya, xb, yb):
    dx = xa - xb
    dy = ya - yb
    angulo_radianes = math.atan2(dy, dx)
    angulo_ajustado = math.fmod(angulo_radianes, (2*math.pi))
    if angulo_ajustado < 0:
        angulo_ajustado += 2*math.pi
    return angulo_ajustado

# Ejemplo de uso:
angulo = calcular_angulo( 0,16,15, 0)
print("El ángulo en radianes desde el punto B hacia el punto A es:", angulo)


data = {
    'T1': {
        'E1': {'x': 1189.9969120812088, 'y': 3440.2314327755917, 'z': 4999.995954488308, 'inclinacion_x': -0.27984398523202003, 'inclinacion_y': -0.19329532557007667, 'cima': False},
        'E2': {'x': -20059.14149092554, 'y': 11249.620707240134, 'z': 4070.0016963695484, 'inclinacion_x': 130.16908630550813, 'inclinacion_y': 79.71906509130696, 'cima': False},
        'E3': {'x': -10159.652375101505, 'y': -8769.096365883212, 'z': 3115.975332998156, 'inclinacion_x': 183.34721276354847, 'inclinacion_y': 184.92885448664708, 'cima': False},
        'E4': {'x': 11195.847543772232, 'y': -20049.66790220844, 'z': 3958.658167610518, 'inclinacion_x': 76.12075459125668, 'inclinacion_y': 134.46078145383177, 'cima': False}
    }
}

def find_entry_with_cima(data):
    for territory, territory_values in data.items():
        for entry, entry_values in territory_values.items():
            if entry_values.get('cima', False):
                return entry
    return None

entry_with_cima = find_entry_with_cima(data)
print(entry_with_cima)
class Escalador :
    def __init__(self,nombre,cuadrante) -> None:
        self.nombre = nombre
        self.cuadrante=cuadrante 
        self.maximo =0
        self.in_maximo=False
        self.in_cuadrante=False
        self.peligro=False
        self.searching_new_maximo=False
    
    def is_incuadrante(self, posicion_x , posicion_y):
        if self.cuadrante==1 and posicion_x>=14000 and posicion_y>=14000:
            self.in_cuadrante=True
        elif self.cuadrante==2 and posicion_x<=-14000 and posicion_y>=14000:
            self.in_cuadrante=True
        elif self.cuadrante==3 and posicion_x<=-14000 and posicion_y<=-14000:
            self.in_cuadrante=True
        elif self.cuadrante==4 and posicion_x>=14000 and posicion_y<=-14000:
            self.in_cuadrante=True

    def new_maximo_angle(self,inclinacion_x, inclinacion_y, posicion_x, posicion_y):
        if posicion_x>0 and posicion_y>0:
            if inclinacion_y <-0.2:
                self.searching_new_maximo=False
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return self.seguir_A(0,posicion_x,0,posicion_y)
        elif posicion_x<0 and posicion_y>0:
            if inclinacion_y <-0.2:
                self.searching_new_maximo=False
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return self.seguir_A(0,posicion_x,0,posicion_y)
        elif posicion_x<0 and posicion_y<0:
            if inclinacion_y >0.2:
                self.searching_new_maximo=False
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return self.seguir_A(0,posicion_x,0,posicion_y)
        elif posicion_x>0 and posicion_y<0:
            if inclinacion_y >0.2:
                self.searching_new_maximo=False
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return self.seguir_A(0,posicion_x,0,posicion_y)
    def peligro_angle(self,inclinacion_x, inclinacion_y, posicion_x, posicion_y):
        if posicion_x>0 and posicion_y>0:
            if inclinacion_y <-2 and inclinacion_x<-2:
                self.peligro=False
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return self.seguir_A(0,posicion_x,0,posicion_y)
        elif posicion_x<0 and posicion_y>0:
            if inclinacion_y <-2 and inclinacion_x>2:
                self.peligro=False
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return self.seguir_A(0,posicion_x,0,posicion_y)
        elif posicion_x<0 and posicion_y<0:
            if inclinacion_y >2 and inclinacion_x>2:
                self.peligro=False
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return self.seguir_A(0,posicion_x,0,posicion_y)
        elif posicion_x>0 and posicion_y<0:
            if inclinacion_y >2 and inclinacion_x <-2:
                self.peligro=False
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return self.seguir_A(0,posicion_x,0,posicion_y)
    def calculate_direction(self, inclinacion_x, inclinacion_y, posicion_x , posicion_y,posicion_z, others_z):
        self.is_incuadrante(posicion_x, posicion_y)
        if self.searching_new_maximo:
            return self.new_maximo_angle(inclinacion_x,inclinacion_y, posicion_x,posicion_y)
        if self.peligro:
            return self.peligro_angle(inclinacion_x,inclinacion_y, posicion_x,posicion_y)
        if self.in_cuadrante:
            self.set_maximo(posicion_z, inclinacion_x, inclinacion_y)
            self.linea_de_fuego(posicion_x,posicion_y)
            if self.in_maximo:
                for esclador_z in others_z:
                    if esclador_z > self.maximo:
                        self.searching_new_maximo=True
                        self.in_maximo=False
                        return self.seguir_A(0,posicion_x,0,posicion_y)
                    
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
    
    
    def set_maximo(self,maximo , inclinacion_x , inclinacion_y):
        if  abs(inclinacion_x)<1 and abs(inclinacion_y)<1 :
            self.maximo = maximo
            self.in_maximo =True


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
        if self.cuadrante==1:
            return pi/4
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
        if math.sqrt(posicon_x*posicon_x + posicion_y*posicion_y) >= 22700:
            self.peligro=True