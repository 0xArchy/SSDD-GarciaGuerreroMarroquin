module IceGauntlet {

	exception Unauthorized {};
	exception NoRoomException {};

	interface Authentication {
		bool authorized = isValid(string token) throws Unauthorized;
		string token = getNewToken(string user, string passHash) throws Unauthorized;
		void changePassword(string user, string currentPassHash, string newPassHash) throws Unauthorized;
	};
	interface RoomService {
		string room = getRoom() throws NoRoomException; 
		void publish(string token, string roomData) throws Unauthorized;
		bool valid = isvalid(string token);
		void remove(string token, string roomName) throws Unauthorized, NoRoomException;

	};
	
};
