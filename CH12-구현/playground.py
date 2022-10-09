[cityCnt, roadCnt, opLen, startCity] = list(map(int, input().split()))
roads = []
dests = []
mids = []
res = []
for i in range(roadCnt):
    roads.append(list(map(int, input().split())))
getConnection(startCity, roads, mids, dests, opLen, 0)
for dest in dests:
    if (dest not in mids):
        res.append(dest)
if (not res):
    print(-1)
else:
    for item in res:
        print(item)