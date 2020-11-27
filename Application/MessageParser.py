from re import match, IGNORECASE
from typing import Tuple, Optional


class MessageParser:
    """Class for Parsing Message"""
    def __init__(self) -> None:
        self.us_pass_split = "|"
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

    def parse_message(self, data: str):
        """Method for parsing message"""
        if self.validate_message(data):
            pass

    def validate_message(self, data: str) -> bool:
        """Method for validating message"""
        if match(self.message_format, data, IGNORECASE):
            return True
        return False

