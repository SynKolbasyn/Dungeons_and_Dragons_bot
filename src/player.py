class Player:
    def __init__(self, data: dict):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.full_name = data["full_name"]
        self.username = data["username"]

    def process_request(self, request: str) -> str:
        return f"id: {self.id}\nfull_name: {self.full_name}\nusername: {self.username}"
