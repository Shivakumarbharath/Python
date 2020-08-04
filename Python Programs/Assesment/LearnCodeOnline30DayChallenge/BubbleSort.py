secs = [56, 55, 60, 78, 55, 36, 79]
x = len(secs)
for i in range(x):
    for j in range(0, x - i - 1):
        if secs[j] > secs[j + 1]:
            secs[j], secs[j + 1] = secs[j + 1], secs[j]

print(secs)
