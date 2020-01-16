testcases = int(input())
a = list()
for i in range(testcases):
    b,c = map(int, input().split())
    a.append([b,c].sort())
a.sort()


answer = a[0][1] - a[0][0]
print(answer)
i = 0
while(i<len(a)):
    for j in range(i+1,len(a)):
        if a[i][0] <= a[j][0]:
            if a[i][1] >= a[j][1]:
                continue
            
        if a[i][1] > a[j][0]:
            answer += a[j][1] - a[i][1]
            i = j
            break
        
        if a[i][1] <= a[j][0]:
            answer += a[j][1] - a[j][0]
            i = j
            break
            
        else:
            print("never")
    i += 1
            
print(answer)
