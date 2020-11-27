from Application.MessageParser import MessageParser


def test_message_validator(message):
    msg = message.get("valid")
    expected = [True for _ in msg]
    result = [MessageParser().validate_message(i) for i in msg]
    assert result == expected


def test_message_invalidator(message):
    msg = message.get("invalid")
    expected = [False for _ in msg]
    result = [MessageParser().validate_message(i) for i in msg]
    assert result == expected


def test_log_valid(log_message):
    msg = log_message.get("valid")
    expected = True
    result = [MessageParser().parse_login(i) for i in msg]
    for i in result:
        if i is None:
            expected = False  # if anyone of the messages is None implies woring message format

    assert expected is True


def test_log_invalid(log_message):
    msg = log_message.get("invalid")
    expected = True
    result = [MessageParser().parse_login(i) for i in msg]
    for i in result:
        if i is not None:
            expected = False  # if anyone of the messages is None implies woring message format

    assert expected is True