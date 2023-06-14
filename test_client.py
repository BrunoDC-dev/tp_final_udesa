from communication.client.client import MountainClient
import math
pi = math.pi
c= MountainClient()
c.add_team('T1', ['E1'])
c.finish_registration()
def inclinacion(inclinacion_x, inclinacion_y):
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

while not c.is_over():
    data = c.get_data()
    print(data)
    inclinacion_x = data['T1']['E1']['inclinacion_x']
    inclinacion_y=  data['T1']['E1']['inclinacion_y']
    direction= inclinacion(inclinacion_x, inclinacion_y)
    if abs(inclinacion_x)<1 or abs(inclinacion_y)<1:
       speed = 50
    else :
       speed = 50   
    c.next_iteration('T1',{'E1':{'direction':direction, 'speed': speed},} )

