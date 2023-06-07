from communication.client.client import MountainClient

c= MountainClient()

c.add_team('T1', ['E1', 'E2', 'E3'])
c.add_team('T2', ['E1', 'E2', 'E3'])
c.finish_registration()
while not c.is_over():
    print(c.get_data())
    c.next_iteration('T1',{'E1':{'direction':0.5}})