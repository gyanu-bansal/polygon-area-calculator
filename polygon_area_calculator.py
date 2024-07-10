class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*self.width+2*self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    def get_picture(self):
        if self.height>50 or self.width >50:
            return "Too big for picture."
        else:
            row='*'*self.width
            return (row+'\n')*self.height
    def get_amount_inside(self,other):
        shape_times=self.get_area() / other.get_area()
        return int(shape_times)
    def set_width(self,num01):
        self.width=num01
    def set_height(self,num01):
        self.height=num01
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
        
    def __str__(self):
        return f"Square(side={self.height})"

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
sq = Square(9)

sq.set_width(7)
print(sq)
