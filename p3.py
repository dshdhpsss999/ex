f = open('17.3.txt')
x1 = int(f.readline())
y1 = int(f.readline())
r = int(f.readline())
kol = int(f.readline())
z= f.readlines()
listt = []
for i in z:
    listt.append(str(i).split(','))
countt = 0
for i in range (0,kol - 1, 2):
    if ((float(listt[i][0]) - x1)**2 + (float(listt[i][1]) - y1)**2 < r**2) and (((float(listt[i+1][0]) - x1)**2 + (float(listt[i+1][1]) - y1)**2 < r**2)):
        countt+=1
print(countt)