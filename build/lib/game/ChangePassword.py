#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Ice
Ice.loadSlice("Icegauntlet.ice")
import IceGauntlet
import os, hashlib, sys
import getpass
from pwn import *
import time

class Client(Ice.Application):

    def run(self,argv):
        proxy = self.communicator().stringToProxy(argv[1])
        authentication = IceGauntlet.AuthenticationPrx.checkedCast(proxy)
        if not authentication:
            raise RuntimeError('Invalid proxy')

        user = argv[2]
        current_password = getpass.getpass(prompt='Current password: ')
        new_password = getpass.getpass(prompt='New password: ')

		#create the hash
        if current_password:
            current_password = hashlib.sha256(current_password.encode()).hexdigest()
        else:
            current_password = None

        new_password = hashlib.sha256(new_password.encode()).hexdigest()
        #get a token
        p = log.progress('Changing password..')
        time.sleep(1)
        try:
            authentication.changePassword(user,current_password,new_password)
            p.status("Commiting changes...")
            time.sleep(1)
            p.success("Password changed")
        except IceGauntlet.Unauthorized:
            p.failure("Password not valid")



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: ./ChangePassword <proxy> <user>")
        sys.exit(1)
    sys.exit(Client().main(sys.argv))
