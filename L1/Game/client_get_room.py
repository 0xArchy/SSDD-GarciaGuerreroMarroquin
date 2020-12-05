#!/usr/bin/python3
# -*- coding: utf-8 -*-
#pylint: disable-msg=w0614
#pylint: disable-msg=e0401
#pylint: disable-msg=c0413

'''
Script that allows to get a room from the interface Dungeon owned by
Icegauntlet.ice
'''

import sys
from pwn import *
import Ice
Ice.loadSlice("Icegauntlet.ice")
import IceGauntlet

class Client(Ice.Application):

    '''
    class Client that allows to get a room from the server and save it
    tmp.json
    '''

    def __save__(self,room):
        with open('tmp.json','w+') as roomfile:
            roomfile.write(room)

    def run(self,argv):
        proxy = self.communicator().stringToProxy(argv[1])
        game = IceGauntlet.DungeonPrx.checkedCast(proxy)
        if not game:
            raise RuntimeError('Invalid proxy')

        try:
            room = game.getRoom()
            print(room)
            self.__save__(room)
        except IceGauntlet.RoomNotExists:
            print("Room not exists")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("usage: ./client_get_room.py <proxy>")
        sys.exit(1)
    sys.exit(Client().main(sys.argv))
