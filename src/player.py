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
        self.state = data["state"]
        # TODO: Сделать sub_state, пример - state - Creating character, sub_state - [Choosing a race, Choosing a class]

    def сhoosing_a_race(self, request: str) -> tuple[str, str, list[list[str]]]:
        match request:
            case _:
                return "Unknown action", f"{PROJECT_DIR}/game_data/images/fantasy-races.png", [[i] for i in RACES]

    def process_request(self, request: str) -> tuple[str, str, list[list[str]]]:
        answer = ""
        image = ""
        buttons = []
        match self.state:
            case "Choosing a race":
                answer, image, buttons = self.сhoosing_a_race(request)
        return answer, image, buttons
