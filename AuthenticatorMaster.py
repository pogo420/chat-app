import json
import sys
from uuid import uuid4


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

    def write_access_key(self):
        '''Method for writing acces key and expiry date'''
        key = self.generate_key()
        user_id = self.user_id
        temp = None
        with open("access-db.json") as f:
            temp = json.load(f)
            temp[user_id]["access-key"] = key

        with open("access-db.json","w") as f:
            json.dump(temp, f)

    def write_exp_date(self):
        '''Method for writing acces key and expiry date'''
        user_id = self.user_id
        # current_date = ""
        temp = None
        with open("access-db.json") as f:
            temp = json.load(f)
            temp[user_id]["expiry-date"] = key

        with open("access-db.json","w") as f:
            json.dump(temp, f)

    def generate_key(self):
        '''Method to generate keys'''
        return str(uuid4())

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


if __name__ == "__main__":
    user_id = "1234"
    access_key = "0laph"
    # print(AuthenticatorMaster(user_id, access_key).authenticate())
    # print(AuthenticatorMaster(user_id, access_key).generate_key())
    print(AuthenticatorMaster(user_id, access_key).write_access_key())
