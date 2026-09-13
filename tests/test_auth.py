from utils.auth import AuthManager
import tempfile
import os


def test_register_and_login():

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    auth = AuthManager(users_file=tmp_path)

    user = auth.register(
        "Alex",
        "alex@example.com",
        "1234",
        25,
        70,
        175
    )

    assert user.username == "Alex"
    assert user.email == "alex@example.com"

    try:
        auth.register(
            "Alex",
            "alex@example.com",
            "1234",
            25,
            70,
            175
        )
        assert False
    except ValueError:
        assert True

    logged_in = auth.login("alex@example.com", "1234")

    assert logged_in is not None
    assert logged_in.username == "Alex"

    failed_login = auth.login("alex@example.com", "wrong")

    assert failed_login is None

    os.remove(tmp_path)
