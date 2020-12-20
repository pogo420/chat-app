import pytest
import os


@pytest.fixture(scope="session")
def env_setup():
    db_path = os.environ["CHAT_DB"]
    data = {
        "db_path": db_path,
    }
    yield data


@pytest.fixture(scope="session")
def message():
    test_messages = {
        "valid": [
            "@arnab hello there",
            "@arnab12 Hello there",
            "@Puchu-32      Ola bhai wewewe0909...****"
        ],
        "valid_user_message": [
            ["arnab", "hello there"],
            ["arnab12", "Hello there"],
            ["Puchu-32", "Ola bhai wewewe0909...****"]
        ],
        "invalid": [
            "Hello",
            "@Al",
        ]
    }
    yield test_messages


@pytest.fixture(scope="session")
def log_message():
    test_messages = {
        "valid": [
            "arnab| ola",
            "Puchu | p--nkol"
        ],
        "invalid": [
            "hello pass",
            "hew lo kolo",
            "|kii9-",
            "arnab |   "
        ]
    }
    yield test_messages

@pytest.fixture(scope="session")
def log_cred_test():
    test_messages = {
        "valid": [
            "arnab|ola"
        ],
        "invalid": [
            "arnab|polo"
        ]
    }
    yield test_messages
