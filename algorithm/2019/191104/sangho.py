n, c = map(int, input().split())

sta = input()
cor = input()

num = len(sta)

def start(lis,c,l):
    li = ""
    cost = 0
    n = 0
    answer = []
    for i in range(l):
        li += lis[i]
    while n < l :
        if n != len(li)-2 and (li[n:n+3] == "112" or li[n:n+3] == "211") :
            cost += (c+4)
            answer.append([n+1,n+3])
            # n += 1
            if (li[n:n+3] == "112"):
                li = li[:n] + "2" + li[n+1:]
                li = li[:n+2] + '1' + li[n+3:]
            elif (li[n:n+3] == "211"):
                li = li[:n] + '1' + li[n+1:]
                li = li[:n+2] + '2' + li[n+3:]
        elif n != len(li)-2 and (li[n:n+3] == "122" or li[n:n+3] == "221"):
            # n += 1
            cost += (c+5)
            answer.append([n+1,n+3])
            if (li[n:n+3] == "122"):
                li = li[:n] + '2' + li[n+1:]
                li = li[:n+2] + '1' + li[n+3:]
            elif (li[n:n+3] == "221"):
                li = li[:n] + '1' + li[n+1:]
                li = li[:n+2] + '2' + li[n+3:]
        elif (li[n:n+2] == "12" or li[n:n+2] == "21"):
            n += 1
            cost += (c+3)
            answer.append([n+1,n+2]) 
            if li[n:n+2] == "12" :
                li = li[:n] + '2' + li[n+1:]
                li = li[:n+1] + '1' + li[n+2:]
            elif li[n:n+2] == '21' :
                li = li[:n] + '1' + li[n+1:]
                li = li[:n+1] + '2' + li[n+2:]
        n += 1
        print(li,cost)
    return answer,cost 

def correct(lis,c,l):
    li = ""
    cost = 0
    n = 0
    answer = []
    for i in range(l):
        li += lis[i]
    while n < l :
        if n != len(li)-2 and (li[n:n+3] == "112" or li[n:n+3] == "211") :
            cost += (c+4)
            answer.append([n+1,n+3])
            if (li[n:n+3] == "112"):
                li = li[:n] + "2" + li[n+1:]
                li = li[:n+2] + '1' + li[n+3:]
            elif (li[n:n+3] == "211"):
                li = li[:n] + '1' + li[n+1:]
                li = li[:n+2] + '2' + li[n+3:]
        elif n != len(li)-2 and (li[n:n+3] == "122" or li[n:n+3] == "221"):
            cost += (c+5)
            answer.append([n+1,n+3])
            if (li[n:n+3] == "122"):
                li = li[:n] + '2' + li[n+1:]
                li = li[:n+2] + '1' + li[n+3:]
            elif (li[n:n+3] == "221"):
                li = li[:n] + '1' + li[n+1:]
                li = li[:n+2] + '2' + li[n+3:]
        elif (li[n:n+2] == "12" or li[n:n+2] == "21"):
            cost += (c+3)
            answer.append([n+1,n+2])
            if li[n:n+2] == "12" :
                li = li[:n] + '2' + li[n+1:]
                li = li[:n+1] + '1' + li[n+2:]
            elif li[n:n+2] == '21' :
                li = li[:n] + '1' + li[n+1:]
                li = li[:n+1] + '2' + li[n+2:]
        n += 1
    lit = []
    for i in range(len(answer)):
        lit.append(answer[-(i+1)])
    return lit,cost 

start_list,start_cost = start(sta,c,num)
correct_list,correct_cost =  correct(cor,c,num)

if start_cost < correct_cost :
    print(len(start_list))
    for i in range(len(start_list)) :
        print(start_list[i][0],start_list[i][1])
else:
    print(len(correct_list))
    for i in range(len(correct_list)) :
        print(correct_list[i][0],correct_list[i][1])
