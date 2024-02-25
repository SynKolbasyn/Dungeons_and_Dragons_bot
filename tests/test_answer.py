import pytest
from src.player import Player


@pytest.fixture()
def player():
    return Player()


def test_answer(player: Player):
    assert "test - 1" == player.process_request("test")
