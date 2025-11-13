list1 = [5, 22, -35, 612, 652, -213, -1, 512, 9, 3]
ist = []

for i in list1:
    if i % 2 == 0:
        ist.append(i)

print(ist)

ist2 = []
for i in list1:
    if i % 3 == 0:
        ist2.append(i)

print(ist2)

ist3 = []
for i in list1:
    if i < 0:
        ist3.append(i)
print(ist3)

ist4 = []
for i in list1:
    if i > 0:
        ist4.append(i)
print(ist4)
