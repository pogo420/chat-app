from Application.DbHelper import DbHelper


def test_read_password(env_setup):
    db_path = env_setup.get("db_path")
    passwd = DbHelper(db_path).read_password("arnab")
    assert passwd is not None
