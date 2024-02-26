from os import getenv

from ujson import load


PROJECT_DIR = getenv("PROJECT_DIR")


with open(f"{PROJECT_DIR}/game_data/resources/races.json", "r", encoding="utf-8") as file:
    RACES = load(file)
with open(f"{PROJECT_DIR}/game_data/resources/classes.json", "r", encoding="utf-8") as file:
    CLASSES = load(file)


class Player:
    def __init__(self, data: dict):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.full_name = data["full_name"]
        self.username = data["username"]

    def process_request(self, request: str) -> str:
        return f"{self.username}: {request}"
