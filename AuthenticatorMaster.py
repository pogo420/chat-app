import json
import sys


class AuthenticatorMaster:

    def __init__(self, user_id, access_key):
        self.user_id = user_id
        self.access_key = access_key

    def read_access_key(self, user_id):
        '''Method for reading acces key and expiry date'''
        key = None
        exp_date = None
        with open("access-db.json") as f:
            temp = json.load(f).get(user_id)
            if temp:
                return temp
            return None

    def write_access_key(self, user_id):
        '''Method for writing acces key and expiry date'''
        pass

    def generate_key(self):
        '''Method to generate keys'''
        pass

    def authenticate(self):
        '''Method for authentication'''
        access_data = self.read_access_key(self.user_id)
        if not access_data:
            print("User id:{} not present in db".format(self.user_id))
            sys.exit(0)

        if access_data.get("access-key") == self.access_key:
            if True:  # checking dates
                return (True, "Access verified")
            return (False, "Access key expired")
        return (False, "Access validation failed")

    # def generate_key(self, user_id, access_key):
    #     '''Method for generate access key'''
    #     db = None
    #     key = None
    #     with open("chat-db.json") as f:
    #         db = json.load(f)
    #         if db.get("access_key").get(user_id) == access_key:
    #             key = uuid.uuid4()
    #             db.get("access_key")[user_id] = key
    #         else:
    #             return "-1"
    #
    #     with open("chat-db.json","w") as f:
    #         db = json.dump(f)
    #
    #     return key


if __name__ == "__main__":
    user_id = "1234"
    access_key = "0laph"
    print(AuthenticatorMaster(user_id, access_key).authenticate())
