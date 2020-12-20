from Application.AuthenticationMaster import AuthenticationMaster
from Application.MessageParser import MessageParser


def test_check_authenticate(env_setup, log_cred_test):
    user, passw = MessageParser().parse_login(log_cred_test.get("valid")[0])

    obj = AuthenticationMaster(env_setup.get("db_path"))
    obj.authenticate(user, passw)
    print(user,passw, obj.is_authenticated(user))
    assert obj.is_authenticated(user) is True


def test_check_inval_authenticate(env_setup, log_cred_test):
    user, passw = MessageParser().parse_login(log_cred_test.get("invalid")[0])

    obj = AuthenticationMaster(env_setup.get("db_path"))
    obj.authenticate(user, passw)
    print(user,passw, obj.is_authenticated(user))
    assert obj.is_authenticated(user) is False
