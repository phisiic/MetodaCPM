class Czynnosc:
    def __init__(self, name, duration, before=None, after=None):
        if after is None:
            after = Zdarzenie()
        if before is None:
            before = Zdarzenie()
        self.name = name
        self.duration = duration
        self.before = before
        self.after = after

    def __str__(self):
        before_name = self.before.id
        after_name = self.after.id
        return f"Czynnosc: {self.name}, Duration: {self.duration}, Before: {before_name}, After: {after_name}"

class Zdarzenie:  # kolka
    def __init__(self, id, ti=0, tj=0):
        self.id = id
        self.ti = ti
        self.tj = tj
        self.float = self.tj - self.ti

    def __str__(self):
        return f"Zdarzenie ID: {self.id}, Ti: {self.ti}, Tj: {self.tj}, Float: {self.float}"

    def set_ti(self, ti):
        self.ti = ti

    def set_tj(self, tj):
        self.tj = tj

    def set_float(self):
        self.float = self.tj - self.ti
