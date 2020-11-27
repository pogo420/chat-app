import pytest
import os


@pytest.fixture(scope="session")
def env_setup():
    db_path = os.environ["CHAT_DB"]
    data = {
        "db_path": db_path,
    }
    yield data
