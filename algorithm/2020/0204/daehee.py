n = int(input())

floor = [[0 for j in range(101)] for i in range(101)]
papers = list()
for i in range(n):
    x, y, w, h = map(int, input().split())
    for a in range(x,x+w):
        for b in range(y,y+h):
            floor[a][b] = i+1
    papers.append([x,y,w,h])


for idx, paper in enumerate(papers):
    value = 0
    for x in range(paper[0], paper[0]+paper[2]):
        value += floor[x].count(idx+1)
        
    print(value)
