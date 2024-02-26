import pytest
from src.player import Player


@pytest.fixture()
def player():
    data = {
        "id": 0,
        "first_name": "empty",
        "last_name": "empty",
        "full_name": "empty",
        "username": "empty",
        "state": "Choosing a race"
    }
    return Player(data)


def test_answer(player: Player):
    answer, _, _ = player.process_request("/start")
    assert "Unknown action" == answer
