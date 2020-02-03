num=int(input())

lst = [[0 for i in range(101)] for j in range(101)]  # * 사용하지 말것. *는 얕은 복사이다. 
count = 1

for i in range(num):
    x,y,width,height = map(int, input().split())
    for j in range(x,x+width) :
        for k in range(y,y+height) : 
            lst[j][k] = count
    count+=1        # https://hashcode.co.kr/questions/277/%ED%95%98%EA%B8%B0 

count = 1
for i in range(num):
    area = 0
    for j in range(101):
        area += lst[j].count(count)
    print(area)
    count +=1