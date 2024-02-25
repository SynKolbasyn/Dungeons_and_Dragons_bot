class Player:
    def __init__(self):
        self.counter = 0

    def process_request(self, request: str) -> str:
        self.counter += 1
        return f"{request} - {self.counter}"
