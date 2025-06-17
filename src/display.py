class Display:
    def __init__(self, id, data=None , is_on=False):
        self.id = id
        self.data = data or {}
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: {self.data}"

    def update(self, data):
        self.data = data
        for key, value in data.items():
            print(f"{key}: {value}")