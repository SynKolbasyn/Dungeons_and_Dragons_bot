import pytest
from src.player import Player


@pytest.fixture()
def player():
    data = {"id": 0, "first_name": "empty", "last_name": "empty", "full_name": "empty", "username": "empty"}
    return Player(data)


def test_answer(player: Player):
    assert "empty: test" == player.process_request("test")
