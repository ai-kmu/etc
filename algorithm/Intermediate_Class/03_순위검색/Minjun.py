# 시간 초과
# O(N^2)의 한계 . . . .
# 잊지 않겠습니다 순위검색 . . .

def solution(info, query):
    answer = []
    
    info = list(map(lambda x: x.split(), info))
    query = list(map(lambda x: x.split(), query))

    for i in query:
        cnt = 0
        for j in info:
            # 언어 비교
            if i[0] != "-":
                if i[0] != j[0]:
                    continue
            # 직군 비교
            if i[2] != "-":
                if i[2] != j[1]:
                    continue
            # 경력 비교
            if i[4] != "-":
                if i[4] != j[2]:
                    continue
            # 소울푸드 비교
            if i[6] != "-":
                if i[6] != j[3]:
                    continue
            # 점수 비교
            if int(j[4]) >= int(i[7]):
                cnt += 1
        answer.append(cnt)
    return answer
