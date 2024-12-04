f = open('17.0.txt')
listt0 = []
for i in range (4):
    q = f.readline().split(',')
    listt0.append(q)
kol = int(f.readline())
z= f.readlines()
listt = []

for i in z:
    listt.append(str(i).split(','))
countt = 0
for i in range (kol):
    if ((float(listt[i][0]) < float(listt0[0][0]) and float(listt[i][1]) < float(listt0[0][1])) and (float(listt[i][0]) > float(listt0[1][0]) and float(listt[i][1]) < float(listt0[1][1])) and (float(listt[i][0]) > float(listt0[2][0]) and float(listt[i][1]) > float(listt0[2][1])) and (float(listt[i][0]) < float(listt0[3][0]) and float(listt[i][1]) > float(listt0[3][1]))):
        countt+=1
print(countt)
