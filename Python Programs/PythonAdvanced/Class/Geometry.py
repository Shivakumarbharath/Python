class Line:
    def __init__(self,coord1=(0,0),coord2=(0,0)):
        self.coord1=tuple(coord1)
        self.coord2 = tuple(coord2)
        self.x1=coord1[0]
        self.y1 = coord1[1]
        self.x2 = coord2[0]
        self.y2 = coord2[1]

    def distance(self):
        #√ (x2 − x1)2 + (y2 − y1)2
        dist=((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5
        return dist

    def slope(self):
        m=(self.y2-self.y1)/(self.x2-self.x1)
        return m

l1=Line((3,2),(8,10))
print(l1.distance(),l1.slope())


class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius

    def volume(self):
        return 3.14*self.radius*2*self.height

    def surfacearea(self):
        return (2*3.14*self.radius*self.height+2*3.140*self.radius**2)

c=Cylinder()
print(c.surfacearea())
print(c.volume())
