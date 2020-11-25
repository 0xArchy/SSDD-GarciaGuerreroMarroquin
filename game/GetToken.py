import Ice
Ice.loadSlice("Icegauntlet.ice")
import IceGauntlet
import os, hashlib, sys

class Client(Ice.Application):

	def run(self,argv):
		proxy = self.communicator().stringToProxy(argv[1])
		authentication = IceGauntlet.AuthenticationPrx.checkedCast(proxy)
		if not authentication:
			raise RuntimeError('Invalid proxy')

		user = argv[2]
		password = argv[3]

		#create a password_hash
		salt = os.urandom(32)
		password_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
		#get a token
		token = authentication.getNewToken(user, 'lol')
		print(token)



if __name__ == "__main__":

	if len(sys.argv) != 4:
		print("usage: ./GetToken <proxy> <user> <password>")
		sys.exit(1)
	sys.exit(Client().main(sys.argv))
