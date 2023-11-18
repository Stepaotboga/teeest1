import sqlite3


con = sqlite3.connect('listening.db')
cur = con.cursor()
result = cur.execute('''SELECT state, rank, place FROM Rules''').fetchall()
data = []
data1 = []
for elem in result:
    data.append(elem[0])
    data1.append(list(elem[1:]))
con.close()
a = []
for i in range(int(input())):
    dt = input().split()
    if dt[-1] in data:
        w = data.index(dt[-1])
        a.append(f'{dt[0]}({data1[w][0]}) - {data1[w][1]}')
    else:
        a.append(f'{dt[0]} - You do not belong here!')
print('\n'.join(a))