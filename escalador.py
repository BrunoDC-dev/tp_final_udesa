import random
import math
pi = math.pi
class Escalador :
    def __init__(self,nombre,cuadrante) -> None:
        self.nombre = nombre
        self.cuadrante=cuadrante 
        self.peligro=False
        self.searching_new_maximo=False
        self.points_to_go=[]
        self.dispersarse=600
        self.iteraciones_hasta_salir_peligro=0
        self.ultimos_z=[]
        self.inclinaxion_x=[]
        self.inclinaxion_y=[]
        self.agregar_puntos_para_ir()
                    
    def angulo_peligro(self, inclinacion_x: float, inclinacion_y: float, posicion_x: float, posicion_y: float) -> float:
        """
        Calcula el ángulo cuando el Escalador está en peligro.

        Args:
            inclinacion_x (float): Inclinación en el eje x.
            inclinacion_y (float): Inclinación en el eje y.
            posicion_x (float): Posición en el eje x.
            posicion_y (float): Posición en el eje y.

        Returns:
            float: El ángulo en radianes para evitar el peligro.
        """
        direccion= self.calcular_angulo(posicion_x, posicion_y,self.points_to_go[0][0], self.points_to_go[0][1])
        if self.iteraciones_hasta_salir_peligro>0:
   
                self.iteraciones_hasta_salir_peligro-=1
                #print("iteraciones" ,self.iteraciones_hasta_salir_peligro, "Angulo", self.calcular_angulo(posicion_x, posicion_y,self.points_to_go[0][0], self.points_to_go[0][1]))
                return direccion
   
        else:
                if pi/2 > direccion >=0:
                    if inclinacion_x > 0 and inclinacion_y>0:
                       
                        self.peligro=False
                        
                        return self.inclinacion(inclinacion_x,inclinacion_y)
                    else: 
                        return direccion
                elif pi>direccion >=pi/2:
                    if inclinacion_y >0  and inclinacion_x<0: 
                       
                        self.peligro=False
                        
                        return self.inclinacion(inclinacion_x,inclinacion_y)
                    else: 
                        return direccion  
                elif 3*pi/2>direccion>=pi:
                    if inclinacion_x<0 and inclinacion_y<0:
                       
                        self.peligro=False
                        
                        return self.inclinacion(inclinacion_x,inclinacion_y)
                    else: 
                        return direccion
                elif 2*pi>direccion>=3*pi/2 :
                    if inclinacion_y<0 and inclinacion_x>0:
                       
                        self.peligro=False
                        
                        return self.inclinacion(inclinacion_x,inclinacion_y)
                    else: 
                        return direccion
    
    
    def calcular_direccion(self, inclinacion_x: float, inclinacion_y: float, posicion_x: float, 
                            posicion_y: float,posicion_z: float) -> float:
        """
        Calcula la dirección en la que debe moverse el Escalador.

        Args:
            inclinacion_x (float): Inclinación en el eje x.
            inclinacion_y (float): Inclinación en el eje y.
            posicion_x (float): Posición en el eje x.
            posicion_y (float): Posición en el eje y.
            posicion_z (float): Posición en el eje z.
            others_z (list[float]): Lista de posiciones en el eje z de otros escaladores.

        Returns:
            float: El ángulo en radianes para la dirección en la que debe moverse el Escalador.
        """
        if len(self.points_to_go) >0:
            #print(self.points_to_go)
            self.punto_de_control(posicion_x,posicion_y)
        if len(self.points_to_go)==0:
            #print("Estoy aca")
            new_point_x, new_point_y = self.puntos_en_circunferencia(22000)
            self.points_to_go.append([new_point_x,new_point_y])
        
        self.linea_de_fuego(posicion_x,posicion_y)
        if self.peligro:
            #print(self.nombre, "etoy en peligro")
            return self.angulo_peligro(inclinacion_x,inclinacion_y, posicion_x,posicion_y)    
        
        if self.dispersarse>0:
        
            self.dispersarse -=1
           # print(self.nombre, " Me estoy dispersando")
            return self.calcular_angulo(posicion_x, posicion_y,self.points_to_go[0][0], self.points_to_go[0][1])
        
        else:
           
            return self.maximo_local( posicion_x, posicion_y, inclinacion_x, inclinacion_y)
        
        
    def punto_de_control(self, posicion_x: float, posicion_y: float) -> None:
        """
        Verifica si se ha alcanzado un punto de referencia y lo elimina de la lista.

        Args:
            posicion_x (float): Posición en el eje x.
            posicion_y (float): Posición en el eje y.
        """

        x_gotten =False
        y_gotten = False
        
        if self.points_to_go[0][0]>0:
        
            if posicion_x > self.points_to_go[0][0]-100:
                x_gotten=True
        
        else:
        
              if posicion_x < self.points_to_go[0][0]+100:
                x_gotten=True
        
        if self.points_to_go[0][1]>0:
        
            if  posicion_y > self.points_to_go[0][1]-100:
                y_gotten=True
        
        else:
        
              if posicion_y < self.points_to_go[0][1]+100:
                y_gotten=True
        
        if x_gotten and y_gotten :
        
            self.points_to_go= self.points_to_go[1:]
    
    def inclinacion(self, inclinacion_x: float, inclinacion_y: float) -> float:
        """
        Calcula el ángulo de inclinación.

        Args:
            inclinacion_x (float): Inclinación en el eje x.
            inclinacion_y (float): Inclinación en el eje y.

        Returns:
            float: El ángulo en radianes de la inclinación.
        """

       
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

    
    def calcular_angulo(self, posicion_x: float, posicion_y: float, objetivo_x: float, objetivo_y: float) -> float:
        """
        Calcula el ángulo hacia un objetivo dado.

        Args:
            posicion_x (float): Posición en el eje x.
            posicion_y (float): Posición en el eje y.
            objetivo_x (float): Objetivo en el eje x.
            objetivo_y (float): Objetivo en el eje y.

        Returns:
            float: El ángulo en radianes hacia el objetivo.
        """
        dx = objetivo_x - posicion_x
        dy = objetivo_y - posicion_y
        angulo = math.atan2(dy, dx)
       
        if angulo < 0:
            angulo += 2 * math.pi
       
        return angulo
    
    def linea_de_fuego(self, posicion_x: float, posicion_y: float) -> None:
        """
        Verifica si el Escalador está en la línea de fuego y establece la bandera de peligro si es necesario.

        Args:
            posicion_x (float): Posición en el eje x.
            posicion_y (float): Posición en el eje y.
        """
        if math.sqrt(posicion_x*posicion_x + posicion_y*posicion_y) >= 22700:
       
            self.peligro=True
            self.iteraciones_hasta_salir_peligro+=5
   
    def agregar_puntos_para_ir(self):
        if self.cuadrante==1:
            self.points_to_go = [[-6000,21000],[6000,-21000],[-21000,-6000],[21000,-6000],[6000,-21000], [6000,21000],[-21000,-6000]]
        elif self.cuadrante==2:
            self.points_to_go = [[21000,-6000],[-21000,6000],[-6000,-21000],[-6000,21000], [-21000,6000], [21000, 6000], [-6000,-21000]]
             
        elif self.cuadrante==3:
            self.points_to_go = [[-21000,-6000],[-15000,16000],[21000, 6000],[-21000,6000],[6000,21000],[-6000,-21000],[-15000,16000] ]
             
        elif self.cuadrante==4:
            self.points_to_go = [[-6000, -21000],[16000,-15000],[6000,21000],[6000,-21000],[21000,6000],[-21000,-6000],[16000,-15000]]
             
    def puntos_en_circunferencia(self, radius: float) -> tuple[float, float]:
        """
        Calcula un punto en la circunferencia de un círculo dado un radio.

        Args:
            radius (float): El radio del círculo.

        Returns:
            tuple[float, float]: Las coordenadas (x, y) del punto en la circunferencia.
        """
        angle = 2 * pi * random.random()  # Genera anuglos aleatorio entre  0 and 2*pi
      
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
      
        return x, y
    
    def maximo_local (self, posicion_x, posicion_y  , inclinacion_x , inclinacion_y ):
        direccion = self.calcular_angulo(posicion_x,posicion_y ,self.points_to_go[0][0], self.points_to_go[0][1])
        print(direccion)
        if pi/2>direccion>=0:
            if inclinacion_x>0 and inclinacion_y>0:
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return direccion
        elif pi>direccion>=pi/2:
            if inclinacion_x<0 and inclinacion_y>0:
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return direccion
        elif 3*pi/2>direccion>=pi:
            if inclinacion_x<0 and inclinacion_y<0:
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return direccion
        elif 2*pi>direccion>=3*pi/2:
            if inclinacion_x>0 and inclinacion_y<0:
                return self.inclinacion(inclinacion_x,inclinacion_y)
            else:
                return direccion
        else:
            direccion  
    

