from Application.DbHelper import DbHelper


class AuthenticationMaster:
    """Class for managing authentication"""

    def __init__(self, chat_db):
        self.authenticated_user = {}
        self.db_helper = DbHelper(chat_db)

    def authenticate(self,user, password) -> None:
        if password == self.db_helper.read_password(user):
            self.authenticated_user[user] = True
        else:
            pass

    def is_authenticated(self, user) -> bool:
        if self.authenticated_user.get(user) is True:
            return True
        else:
            return False

