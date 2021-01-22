#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#pylint: disable-msg=e0401
#pylint: disable-msg=c0413

'''
Script that runs the server
'''

import sys
import json
import os.path
import logging
import signal
import random
import Ice
Ice.loadSlice('Icegauntlet.ice')
import IceGauntlet
import icegauntlettool

ROOMS_FILE = 'rooms.json'

class GameI(IceGauntlet.Dungeon):

    def __init__(self):
        # Creamos el objeto dungeonArea
        self.dungeonarea = DungeonArea()
        
    def getEntrance(self, current=None):
        return self.dungeonarea

class DungeonArea(IceGauntlet.DungeonArea):
    def __init__(self):
        self.DungeonArea = DungeonArea()
        self._rooms_ = {}
        if os.path.exists(ROOMS_FILE):
            self.refresh()

    def refresh(self):
        '''
        refresh the rooms of the DB
        '''
        #logging.debug('Reloading user database')
        with open(ROOMS_FILE,'r') as contents:
            self._rooms_ = json.load(contents)

    def getEventChannel(self, current=None):

    def getMap(self,current=None):
        map = {}
        if len(self._rooms_) == 0:
            raise IceGauntlet.RoomNotExists()
        lab = random.choice(list(self._rooms_.keys()))
        map['data'] = self._rooms_[lab]['data']
        map['room'] = lab
        return json.dumps(map)

    def getActors(self, current=None):

    def getItems(self, current=None):

    def getNextArea(self):
        return self.DungeonArea

class DungeonAreaSync(IceGauntlet.DungeonAreaSync):
    def __init__():

    def fireEvent(self,event,senderId,current=None):



class Server(Ice.Application):
    '''
    Authentication Server
    '''
    def run(self, argv):
        '''
        Server loop
        '''
        logging.debug('Initializing server...')
        #check authentication proxy
        proxyauth = self.communicator().stringToProxy(argv[1])
        authentication = IceGauntlet.AuthenticationPrx.checkedCast(proxyauth)
        if not authentication:
            raise RuntimeError('Invalid proxy')

        servant = RoomServiceI(authentication)
        signal.signal(signal.SIGUSR1, servant.refresh)

        adapter = self.communicator().createObjectAdapter('ServiceAdapter')
        room_service_identity = self.communicator().stringToIdentity('RoomManager')
        adapter.add(servant,room_service_identity)
        proxy = adapter.createProxy(room_service_identity)
        servant_game = GameI()
        game_identity = self.communicator().stringToIdentity('Dungeon')
        adapter.add(servant_game,game_identity)
        proxygame = adapter.createProxy(game_identity)
        adapter.activate()
        logging.debug('AdapterGame ready, servant proxy: {}'.format(proxy))
        print('"{}"'.format(proxy), flush=True)
        print('"{}"'.format(proxygame), flush=True)

        logging.debug('Entering server loop...')
        self.shutdownOnInterrupt()
        self.communicator().waitForShutdown()

        return 0


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("usage: ./Server.py <proxy>")
        sys.exit(0)

    app = Server()
    sys.exit(app.main(sys.argv))
