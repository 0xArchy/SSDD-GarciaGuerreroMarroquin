module IceGauntlet {

	exception Unauthorized {};
	exception RoomAlreadyExists {};
	exception RoomNotExists {};

	interface Authentication {
		bool isValid(string token) throws Unauthorized;
		string getNewToken(string user, string passHash) throws Unauthorized;
		void changePassword(string user, string currentPassHash, string newPassHash) throws Unauthorized;
	};
	interface RoomService {
		string getRoom(); 
		void publish(string token, string roomData) throws Unauthorized, RoomAlreadyExists;
		bool isvalid(string token);
		void remove(string token, string roomName) throws Unauthorized, RoomNotExists;

	};
	interface Game {
		string getRoom() throws RoomNotExists;
	};
};
