module IceGauntlet {

	exception Unauthorized {};
	exception RoomAlreadyExists {};
	exception RoomNotExists {};
	exception WrongRoomFormat {};

	interface Authentication {
		bool isValid(string token);
		string getNewToken(string user, string passHash) throws Unauthorized;
		void changePassword(string user, string currentPassHash, string newPassHash) throws Unauthorized;
	};
	interface RoomManager { 
		void publish(string token, string roomData) throws Unauthorized, RoomAlreadyExists, WrongRoomFormat;
		void remove(string token, string roomName) throws Unauthorized, RoomNotExists;

	};
	interface Game {
		string getRoom() throws RoomNotExists;
	};
};
