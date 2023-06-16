
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
print(seguir_A(1190.0798098699024, -19601.599168381374, 3440.17408793893, 11951.67572))

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
angulo = calcular_angulo( 1190.0798098699024, 3440.17408793893, -19601.599168381374,  11951.67572)
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
