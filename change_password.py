#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#pylint: disable-msg=e0401
#pylint: disable-msg=c0413

'''
Script for change user password
'''

import hashlib
import sys
import time
import getpass
from pwn import log
import Ice
Ice.loadSlice("Icegauntlet.ice")
import IceGauntlet


class Client(Ice.Application):

    '''
    Client class for change user password
    '''

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
        variable_progress = log.progress('Changing password..')
        time.sleep(1)
        try:
            authentication.changePassword(user,current_password,new_password)
            variable_progress.status("Commiting changes...")
            time.sleep(1)
            variable_progress.success("Password changed")
        except IceGauntlet.Unauthorized:
            variable_progress.failure("Password not valid")



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: ./ChangePassword <proxy> <user>")
        sys.exit(1)
    sys.exit(Client().main(sys.argv))
