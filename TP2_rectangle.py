class Form:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
class Rectangle(Form):
    def aire(self):
        return self.largeur * self.hauteur
class Triangle(Form):
    def aire(self):
        return self.largeur * self.hauteur/2
rectangle = Rectangle(15,7)
print(f"la surface de cette rectangle est de: {rectangle.aire()}")
triangle = Triangle(9,9)
print(f"la surface de cetete triangle est de: {triangle.aire()}")