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

    
    from Polygon import Polygon


def main():

    sides = Polygon(input("Number of sides for first polygon: "))
    poly2 = Polygon(input("Number of sides for second polygon: "))

    addition = sides + poly2
    subtraction = sides - poly2
    greater = sides > poly2
    lessThen = sides < poly2
    equal = sides == poly2
    leng = addition

    print(addition)
    print(subtraction)
    print(greater)
    print(lessThen)
    print(equal)
    print(len(leng))


main()
