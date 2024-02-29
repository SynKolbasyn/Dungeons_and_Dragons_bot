import pytest
from src.player import Player

from os import getenv
from ujson import load


PROJECT_DIR = getenv("PROJECT_DIR")


with open(f"{PROJECT_DIR}/game_data/resources/races.json", "r", encoding="utf-8") as file:
    RACES = load(file)
with open(f"{PROJECT_DIR}/game_data/resources/classes.json", "r", encoding="utf-8") as file:
    CLASSES = load(file)


@pytest.fixture()
def player():
    global PROJECT_DIR
    data = {}
    with open(f"{PROJECT_DIR}/game_data/resources/zero_player.json", "r", encoding="utf-8") as file:
        zero_player = load(file)
        for i in zero_player:
            data[i] = zero_player[i]["val"]
    return Player(data)


def test_answer_race(player: Player):
    answer, _, _ = player.process_request("/start")
    assert "Choose a race" == answer


def test_buttons_race(player: Player):
    global RACES
    _, _, buttons = player.process_request("/start")
    assert [[i] for i in RACES] == buttons


def test_image_race(player: Player):
    _, image, _ = player.process_request("/start")
    assert f"{PROJECT_DIR}/game_data/images/fantasy-races.png" == image


def test_answer_class(player: Player):
    player.sub_state = "Chooses a class"
    answer, _, _ = player.process_request("/start")
    assert "Choose a class" == answer


def test_buttons_class(player: Player):
    global RACES
    player.sub_state = "Chooses a class"
    _, _, buttons = player.process_request("/start")
    assert [[i] for i in CLASSES] == buttons


def test_image_class(player: Player):
    player.sub_state = "Chooses a class"
    _, image, _ = player.process_request("/start")
    assert f"{PROJECT_DIR}/game_data/images/character-classes.png" == image
