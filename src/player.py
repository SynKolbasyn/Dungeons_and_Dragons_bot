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
        self.sub_state = data["sub_state"]

    def choose_race(self, request: str) -> tuple[str, str, list[list[str]]]:
        if request in RACES.keys():
            # TODO: Нагенерить картинки рас и отправлять их в зависимости от выбора игрока
            # TODO: Написать описание расы и отправлять его в зависимости от выбора игрока
            return "Сonfirm the choice of the race?", f"{PROJECT_DIR}/game_data/images/fantasy-races.png", [["Back", "Confirm"]]
        if request == "confirm race":
            self.sub_state = "Chooses a class"
            return "Choose a class", f"{PROJECT_DIR}/game_data/images/fantasy-races.png", [[i] for i in CLASSES]
        if request == "Back to races":
            return "Choose a race", f"{PROJECT_DIR}/game_data/images/fantasy-races.png", [[i] for i in RACES]
        return "Choose a race", f"{PROJECT_DIR}/game_data/images/fantasy-races.png", [[i] for i in RACES]

    def create_character(self, request: str) -> tuple[str, str, list[list[str]]]:
        match self.sub_state:
            case "Chooses a race":
                return self.choose_race(request)
            case _:
                return "Unknown action", f"{PROJECT_DIR}/game_data/images/fantasy-races.png", [[i] for i in RACES]

    def process_request(self, request: str) -> tuple[str, str, list[list[str]]]:
        answer = ""
        image = ""
        buttons = []
        match self.state:
            case "Creates a character":
                answer, image, buttons = self.create_character(request)
            case _:
                answer, image, buttons = "ERROR", f"{PROJECT_DIR}/game_data/images/fantasy-races.png", [[i] for i in RACES]
        return answer, image, buttons
