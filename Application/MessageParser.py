# Not used in current version

from re import match, IGNORECASE
from typing import Tuple, Optional


class MessageParser:
    """Class for Parsing Message"""
    def __init__(self) -> None:
        self.us_pass_split = "|"
        self.user_ref = "@"
        self.message_format = r"^@[-a-z0-9_]+\s+\w.*$"

    def parse_login(self, data: str) -> Optional[Tuple[str, str]]:
        """Method for parsing login"""
        try:
            user, passwd = data.split(self.us_pass_split)
            if len(user) == 0 or user.strip() == "":
                return None
            elif len(passwd) == 0 or passwd.strip() == "":
                return None
            else:
                return user, passwd
        except Exception:
            return None

    def extract_to_message(self, data: str) -> Tuple[str, str]:
        user = ""
        message = ""
        user_flag = False
        for i in data:
            if i == self.user_ref:
                user_flag = True
            elif user_flag == True and i == " ":
                user_flag = False
            elif user_flag:
                user += i
            else:
                message += i
        return user.strip(), message.strip()

    def parse_message(self, data: str) -> Optional[Tuple[str, str]]:
        """Method for parsing message"""
        to = None
        message = None
        if self.validate_message(data):
            to, message = self.extract_to_message(data)
        return to, message

    def validate_message(self, data: str) -> bool:
        """Method for validating message"""
        if match(self.message_format, data, IGNORECASE):
            return True
        return False

