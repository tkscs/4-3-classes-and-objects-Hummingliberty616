import turtle
class Point:
    def __init__ (self,name):
        self.name = name
        self.x = int(name[1])
        self.y = int(name[3])
    
    def __str__ (self):
        return (self.name)
    
    def draw(self):
        turtle.goto(self.x,self.y)
    
point = Point("(0,0)")
point_2 = Point("(100,0)")
point_3 = Point("(100,100)")
point_4 = Point("(0,100)")

print(point)
print(point_2)
print(point_3)
print(point_4)

point.draw()
point_2.draw()
point_3.draw()
point_4.draw()