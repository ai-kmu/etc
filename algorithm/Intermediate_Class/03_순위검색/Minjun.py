# 하드코딩을 해봐도 시간초과를 어찌할 수 없었습니다.
# 잊지 않겠습니다 순위검색 . . .

def solution(info, query):
    answer = []
    person = []
    que = []
    for p in info:
        person.append(p.split())
    for q in query:
        que.append(q.split(" and "))

    for q in que:
        q.append(q[-1].split()[0])
        q.append(q[-2].split()[1])
        q.pop(-3)

    for i in que:
        cnt = 0
        for j in person:
            if i[0] != "-":
                if i[0] != j[0]:
                    continue
            if i[1] != "-":
                if i[1] != j[1]:
                    continue
            if i[2] != "-":
                if i[2] != j[2]:
                    continue
            if i[3] != "-":
                if i[3] != j[3]:
                    continue
            if int(j[4]) >= int(i[4]):
                cnt+=1
        answer.append(cnt)
    return answer            
