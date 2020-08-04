from datetime import *

d = date(2000, 11, 2)
t = time(18, 10)

dt = datetime.combine(d, t)

print(dt)
