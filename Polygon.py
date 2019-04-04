class Polygon():
    def __init__(self,sides = ""):
        self.sides = sides

    def __add__(self,other):
        return self.sides + other.sides

    def __sub__(self,other):
        return self.sides - other.sides

    def __gt__(self,other):
        return self.sides > other.sides

    def __lt__(self,other):
        return self.sides < other.sides

    def __eq__(self,other):
        return self.sides == other.sides
    def __len__(self):
        return self.sides
    def __str__(self):
        return self.sides
