#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#pylint: disable-msg=e0401
#pylint: disable-msg=c0413

'''
Script for change user token
'''

import os
import hashlib
import sys
import getpass
import json
import Ice
Ice.loadSlice("Icegauntlet.ice")
import IceGauntlet

class Client(Ice.Application):

    '''
    This class change user token and raising exceptions if
    the user password and token is invalid
    '''

    def run(self,argv):
        proxy = self.communicator().stringToProxy(argv[2])
        authentication = IceGauntlet.AuthenticationPrx.checkedCast(proxy)
        if not authentication:
            raise RuntimeError('Invalid proxy')

        user = argv[1]
        password = getpass.getpass('Enter password:')
        password = hashlib.sha256(password.encode()).hexdigest()
        try:
            found = False
            token = authentication.getNewToken(user, password)
		    # escribimos el token en nuestro archivo de usuarios y tokens
            # Si no existe creamos el fichero
            if not os.path.exists('tokens.json'):
                # si no existe lo creamos
                data = {
                    "users":[]
                }
                self.write_json(data)

            with open('tokens.json') as file:
                data = json.load(file)
                users = data["users"]
                for i in users:
                    if user in i['user']:
                        i['token'] = token
                        found = True
                        self.write_json(data)
                if found is False:
                    newdata = {
                        'user' : user,
                        'token': token
                    }
                    users.append(newdata)
                    self.write_json(data)
            print(token)

        except IceGauntlet.Unauthorized:
            print("User or password not valid")


    def write_json(self,data, filename='tokens.json'):

        '''
        write_json allows to write in tokens.json the new token
        '''

        with open(filename,'w') as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":


    if len(sys.argv) != 3:
        print("usage: ./GetNewToken <user> <proxy>")
        sys.exit(1)

    sys.exit(Client().main(sys.argv))
