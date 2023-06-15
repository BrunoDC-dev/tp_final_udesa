
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
print(seguir_A(-40,-60,-40,-20))