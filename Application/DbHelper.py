# Not used in current version

from json import load


class DbHelper:
    """class for Db maintenance"""
    def __init__(self, db_name: str):
        self.db_name = db_name

    def read_password(self, user_name):
        """Method for reading password"""
        with open(self.db_name) as f:
            for i in load(f):
                if i.get('user') == user_name:
                    return i.get("pass")
        return

