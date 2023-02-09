class Ficha:
    def __init__(self, value: str):
        self.x = 0
        self.y = 0
        self.val = value

    def chequear_rango(self):
        return 0 <= self.x <= 2 and 0 <= self.y <= 2

    def __str__(self):
        return f"{self.val}"

