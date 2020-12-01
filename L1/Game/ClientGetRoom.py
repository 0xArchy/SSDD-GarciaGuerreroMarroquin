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

    def run(self,argv):
        proxy = self.communicator().stringToProxy(argv[1])
        game = IceGauntlet.GamePrx.checkedCast(proxy)
        if not game:
            raise RuntimeError('Invalid proxy')

        #token = argv[2]
        #roomData = argv[3]
        p = log.progress("Trying to Push the Room...")
        time.sleep(1)
        try:
            room = game.getRoom()
            p.status("Getting room...")
            time.sleep(1)
            p.success("Done")
            print(room)
        except IceGauntlet.RoomNotExists:
            p.failure("Room not exists")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("usage: ./ClientGetRoom <proxy>")
        sys.exit(1)
    sys.exit(Client().main(sys.argv))
