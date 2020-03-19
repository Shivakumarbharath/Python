class rectangle:
    pass
class point:
    pass
box=rectangle()
box.width=100
box.height=200
box.corner=point()
box.corner.x=0
box.corner.y=0
def center(rect):
    p=point()
    p.x=rect.corner.x+box.width/2
    p.y=box.corner.y+box.height/2
    return p
center(box)
print(center(box).x,center(box).y)
def growrect(rect,dw,dh):
    rect.width+=dw
    rect.height+=dh
    return rect
newbox=growrect(box,100,50)
print(newbox.width)
print(newbox.height)
ncenter=center(newbox)
print(ncenter.x)0
print(ncenter.y)