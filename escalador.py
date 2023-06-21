import math
pi = math.pi
class Escalador :
    def __init__(self,nombre,cuadrante) -> None:
        self.nombre = nombre
        self.cuadrante=cuadrante 
        self.maximo =0
        self.in_maximo=False
        self.in_cuadrante=False
        self.peligro=False
        self.searching_new_maximo=False
        self.points_to_go=[]
        self.dispersarse=1000
        self.interaciones_hasta_buscar_maximo=0
        self.iteraciones_hasta_salir_peligro=0
        self.add_point_to_go()

    def new_maximo_angle(self,inclinacion_x, inclinacion_y, posicion_x, posicion_y):
        if self.interaciones_hasta_buscar_maximo>0:
                self.interaciones_hasta_buscar_maximo-=1
                print(self.nombre, "estoy siguiendo a")
                return self.calcular_angulo(posicion_x, posicion_y,self.points_to_go[0][0], self.points_to_go[0][1])
        else:
                self.searching_new_maximo=False
                return self.inclinacion(inclinacion_x,inclinacion_y)
    def peligro_angle(self,inclinacion_x, inclinacion_y, posicion_x, posicion_y):
         if self.iteraciones_hasta_salir_peligro>0:
                self.iteraciones_hasta_salir_peligro-=1
                print("iteraciones" ,self.iteraciones_hasta_salir_peligro, "Angulo", self.calcular_angulo(posicion_x, posicion_y,self.points_to_go[0][0], self.points_to_go[0][1]))
                return self.calcular_angulo(posicion_x, posicion_y,self.points_to_go[0][0], self.points_to_go[0][1])
         else:
             self.peligro=False
             return self.inclinacion(inclinacion_x,inclinacion_y)
    
    def calculate_direction(self, inclinacion_x, inclinacion_y, posicion_x , posicion_y,posicion_z, others_z):
        if len(self.points_to_go) >0:
            print(self.points_to_go)
            self.checkpoint(posicion_x,posicion_y)
        else:
            print("Estoy aca")
            self.points_to_go.append([0,0])
        if self.searching_new_maximo:
            print(self.nombre, "Buscando nuevo maximo")
            return self.new_maximo_angle(inclinacion_x,inclinacion_y, posicion_x,posicion_y)
        if self.peligro:
            print(self.nombre, "etoy en peligro")
            return self.peligro_angle(inclinacion_x,inclinacion_y, posicion_x,posicion_y)
        if self.dispersarse>0:
            self.dispersarse -=1
            print(self.nombre, " Me estoy dispersando")
            return self.calcular_angulo(posicion_x, posicion_y,self.points_to_go[0][0], self.points_to_go[0][1])
        else:
            self.set_maximo(posicion_z, inclinacion_x, inclinacion_y)
            self.linea_de_fuego(posicion_x,posicion_y)
            if self.in_maximo:
                for esclador_z in others_z:
                    if esclador_z > self.maximo:
                        self.searching_new_maximo=True
                        self.interaciones_hasta_buscar_maximo+=2000
                        self.in_maximo=False
                        return self.calcular_angulo(posicion_x, posicion_y,self.points_to_go[0][0], self.points_to_go[0][1])
                    
            return self.inclinacion(inclinacion_x, inclinacion_y)
        
    def checkpoint (self, posicion_x , posicion_y):
        x_gotten =False
        y_gotten = False
        if self.points_to_go[0][0]>0:
            if posicion_x > self.points_to_go[0][0]:
                x_gotten=True
        else:
              if posicion_x < self.points_to_go[0][0]:
                x_gotten=True
        
        if self.points_to_go[0][1]>0:
            if  posicion_y > self.points_to_go[0][1]:
                y_gotten=True
        else:
              if posicion_y < self.points_to_go[0][1]:
                y_gotten=True
        if x_gotten and y_gotten :
            print(self.nombre,"Complete un punto")
            print(self.nombre,"Complete un punto")
            print(self.nombre,"Complete un punto")
            print(self.nombre,"Complete un punto")
            print(self.nombre,"Complete un punto")
            print(self.nombre,"Complete un punto")
            print(self.nombre,"Complete un punto")
            self.points_to_go= self.points_to_go[1:]
    
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
        if  abs(inclinacion_x)<5 and abs(inclinacion_y)<5 :
            print("Encontre un maximo")
            self.maximo = maximo
            self.in_maximo =True

    
    def calcular_angulo(self,x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        angulo = math.atan2(dy, dx)
        if angulo < 0:
            angulo += 2 * math.pi
        return angulo
    
    def linea_de_fuego(self, posicon_x, posicion_y):
        if math.sqrt(posicon_x*posicon_x + posicion_y*posicion_y) >= 22700:
            self.peligro=True
            self.iteraciones_hasta_salir_peligro+=2000
   
    def add_point_to_go(self):
        if self.cuadrante==1:
            self.points_to_go = [[-20000,-5000],[-14000,14000],[-5000,20000],[5000,20000]]
        elif self.cuadrante==2:
            self.points_to_go = [[-14000,14000],[5000,20000],[14000,-14000],[-14000,14000]]
        elif self.cuadrante==3:
            self.points_to_go = [[-5000,-20000],[14000,-14000],[-20000, -5000],[20000,5000]]
        elif self.cuadrante==4:
            self.points_to_go = [[14000,-14000],[20000,5000],[-14000,14000],[14000,-14000]]
