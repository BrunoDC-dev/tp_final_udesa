from communication.client.client import MountainClient

c= MountainClient()

c.add_team('T1', ['E1'])
c.finish_registration()
i=0
while not c.is_over():
    data = c.get_data()
    
    print(data)
    inclinacion_x = data['T1']['E1']['inclinacion_x']
    inclinacion_y=  data['T1']['E1']['inclinacion_y']
    if inclinacion_x<0  and inclinacion_y<0:
        direction = 3.95
    elif inclinacion_x>0  and inclinacion_y>0:
       direction =0.8
    elif inclinacion_x>0  and inclinacion_y<0:
       direction =5.5
    elif inclinacion_x<0  and inclinacion_y>0:
       direction =2.35
    
    if abs(inclinacion_x)<1 or abs(inclinacion_y)<1:
       speed = 10
    else :
       speed = 50   
    c.next_iteration('T1',{'E1':{'direction':direction, 'speed': speed},} )