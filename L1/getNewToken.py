#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Ice
Ice.loadSlice("Icegauntlet.ice")
import IceGauntlet
import os, hashlib, sys
import getpass
from pwn import *
import time,json

class Client(Ice.Application):

    def run(self,argv):
        proxy = self.communicator().stringToProxy(argv[2])
        authentication = IceGauntlet.AuthenticationPrx.checkedCast(proxy)
        if not authentication:
            raise RuntimeError('Invalid proxy')

        user = argv[1]
#        print('Enter password:')
        password = getpass.getpass('p: ')
        '''
        if sys.stdin.isatty():
            password = getpass.getpass('password:')
        else:
            password = input()
        '''

        #create a password_hash
        password = hashlib.sha256(password.encode()).hexdigest()
        #get a token
        p = log.progress("Getting the token...")
#        time.sleep(1)
        try:
            found = False
            token = authentication.getNewToken(user, password)
 #           p.status("Putting the token into a tokens file...")
            time.sleep(1)
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
 #           p.success("Done")
        except IceGauntlet.Unauthorized:
            print("user or paw invalid")
  #          p.failure("User or password not valid")

    def write_json(self,data, filename='tokens.json'):
        with open(filename,'w') as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("usage: ./GetNewToken <user> <proxy>")
        sys.exit(1)

    sys.exit(Client().main(sys.argv))
