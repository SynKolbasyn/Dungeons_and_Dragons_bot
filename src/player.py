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
        self.language = data["language"]
        self.race = data["race"]
        self.clas = data["class"]
        self.lvl = data["lvl"]
        self.exp = data["exp"]
        self.strength = data["strength"]
        self.dexterity = data["dexterity"]
        self.constitution = data["constitution"]
        self.intelligence = data["intelligence"]
        self.wisdom = data["wisdom"]
        self.charisma = data["charisma"]

    def choose_race(self, request: str) -> tuple[str, str, list[list[str]]]:
        if request in RACES.keys():
            # TODO: Нагенерить картинки рас и отправлять их в зависимости от выбора игрока
            # TODO: Написать описание расы и отправлять его в зависимости от выбора игрока
            return "Confirm the choice of the race?", f"{PROJECT_DIR}/game_data/images/fantasy-races.png", [["Back", "Confirm"]]
        if request == "Confirm":
            self.sub_state = "Chooses a class"
            return "Choose a class", f"{PROJECT_DIR}/game_data/images/character-classes.png", [[i] for i in CLASSES]
        if request == "Back":
            return "Choose a race", f"{PROJECT_DIR}/game_data/images/fantasy-races.png", [[i] for i in RACES]
        return "Choose a race", f"{PROJECT_DIR}/game_data/images/fantasy-races.png", [[i] for i in RACES]

    def choose_class(self, request: str) -> tuple[str, str, list[list[str]]]:
        if request in CLASSES.keys():
            # TODO: Нагенерить картинки рас и отправлять их в зависимости от выбора игрока
            # TODO: Написать описание расы и отправлять его в зависимости от выбора игрока
            return "Confirm the choice of the class?", f"{PROJECT_DIR}/game_data/images/character-classes.png", [["Back", "Confirm"]]
        if request == "Confirm":
            self.sub_state = "Chooses a class"
            return "Choose a class", f"{PROJECT_DIR}/game_data/images/character-classes.png", [[i] for i in CLASSES]
        if request == "Back":
            return "Choose a class", f"{PROJECT_DIR}/game_data/images/character-classes.png", [[i] for i in CLASSES]
        return "Choose a class", f"{PROJECT_DIR}/game_data/images/character-classes.png", [[i] for i in CLASSES]

    def create_character(self, request: str) -> tuple[str, str, list[list[str]]]:
        match self.sub_state:
            case "Chooses a race":
                return self.choose_race(request)
            case "Chooses a class":
                return self.choose_class(request)
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
