from models.goal import Goal


def test_goal_creation():
    goal = Goal("Lose weight", "Lose 5kg")

    assert goal.title == "Lose weight"
    assert goal.description == "Lose 5kg"
    assert goal.status == "not done"


def test_goal_complete():
    goal = Goal("Run", "Run 5km daily")

    goal.complete()

    assert goal.status == "done"


def test_goal_to_dict():
    goal = Goal("Gain muscle", "Go to gym")

    data = goal.to_dict()

    assert data["title"] == "Gain muscle"
    assert data["description"] == "Go to gym"
    assert data["status"] == "not done"


def test_goal_str_contains_title():
    goal = Goal("Yoga", "Morning yoga")

    assert "Yoga" in str(goal)
