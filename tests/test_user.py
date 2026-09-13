from models.user import User
from models.goal import Goal


def test_user_creation():
    user = User(
        "Alex",
        "alex@example.com",
        "1234",
        25,
        70,
        175
    )

    assert user.username == "Alex"
    assert user.email == "alex@example.com"
    assert user.age == 25
    assert user.weight == 70
    assert user.height == 175
    assert user.role == "user"


def test_password_is_hashed():
    user = User(
        "Alex",
        "alex@example.com",
        "1234",
        25,
        70,
        175
    )

    assert user.get_password() != "1234"
    assert len(user.get_password()) == 64


def test_check_password():
    user = User(
        "Alex",
        "alex@example.com",
        "1234",
        25,
        70,
        175
    )

    assert user.check_password("1234") is True
    assert user.check_password("wrong") is False


def test_set_password():
    user = User(
        "Alex",
        "alex@example.com",
        "1234",
        25,
        70,
        175
    )

    user.set_password("5678")

    assert user.check_password("5678") is True
    assert user.check_password("1234") is False


def test_add_goal():
    user = User(
        "Alex",
        "alex@example.com",
        "1234",
        25,
        70,
        175
    )

    goal = Goal("Lose weight", "Lose 5kg")

    user.add_goal(goal)

    assert goal in user.goals


def test_update_weight():
    user = User(
        "Alex",
        "alex@example.com",
        "1234",
        25,
        70,
        175
    )

    user.update_weight(65)

    assert user.weight == 65


def test_set_trainer():
    user = User(
        "Alex",
        "alex@example.com",
        "1234",
        25,
        70,
        175
    )

    user.set_trainer("James")

    assert user.trainer == "James"


def test_user_to_dict():
    user = User(
        "Alex",
        "alex@example.com",
        "1234",
        25,
        70,
        175
    )

    data = user.to_dict()

    assert data["username"] == "Alex"
    assert data["email"] == "alex@example.com"
    assert data["age"] == 25
    assert data["weight"] == 70
    assert data["height"] == 175
    assert data["role"] == "user"
    assert "password_hash" in data

