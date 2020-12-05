import json,random

with open('rooms.json','r') as contents:
    data = json.load(contents)
    if len(data) == 0:
         raise IceGauntlet.RoomNotExists()
    print(len(data))
    size = len(data)
    lab = random.randint(0,size-1)
    print(lab)

