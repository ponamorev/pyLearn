i = 0

while i <= 10:
    print(i)
    i += 2

i = 1000

while i > 100:
    print(i)
    i /= 2

for j in 'hello world':
    print(j * 2, end='')

print()
for j in 'hello world':
    if j == 'w':
        continue
    print(j * 3, end='')

print()
for j in 'yamaha, yomasol':
    if j == ',':
        break
    print(j * 4, end='')

print()
for j in 'bugagashenka':
    if j == 'o':
        break
else:
    print("There is no letter \'o\' in \'bugagashenka\'")
