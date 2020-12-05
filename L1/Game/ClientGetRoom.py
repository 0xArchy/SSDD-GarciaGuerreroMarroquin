#!/usr/bin/python3
# -*- coding: utf-8 -*-
import Ice
Ice.loadSlice("Icegauntlet.ice")
import IceGauntlet
import os, hashlib, sys
import getpass
from pwn import *
import time,json,random

class Client(Ice.Application):

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
            '''
            Now We try to save the game in a tmp.json file 
            '''
            print(room)
            self.__save__(room)
        except IceGauntlet.RoomNotExists:
            print("Room not exists")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("usage: ./ClientGetRoom <proxy>")
        sys.exit(1)
    sys.exit(Client().main(sys.argv))
