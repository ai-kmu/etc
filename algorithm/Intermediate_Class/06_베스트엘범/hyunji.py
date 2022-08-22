def solution(genres, plays):
    answer = []
    # 장르가 key, [plays[i], i] 가 value인 딕셔너리
    dic = {}
    # 장르별 plays 총 횟수를 저장한 딕셔너리
    sum_dic = {}
    
    # dic와 sum_dic에 각각 value 집어넣기
    for i in range(len(genres)):
        if genres[i] not in dic.keys():
            dic[genres[i]] = [[plays[i], i]]
            sum_dic[genres[i]] = plays[i]
        else:   
            dic[genres[i]] += [[plays[i], i]]
            sum_dic[genres[i]] += plays[i]
    
    # dic 정렬
    # lambda를 사용해서 장르별로 우선 재생 횟수를 내림차순 정렬
    # 재생 횟수가 동일한 경우는 index(고유번호)로 오름차순 정렬
    for k in dic.keys():
        dic[k] = sorted(dic[k], key = lambda x: (-x[0], x[1]))
    
    # 장르별로 총 재생 횟수를 기준으로 내림차순 정렬
    sum_dic = sorted(sum_dic.items(), key = lambda x: x[1], reverse=True)
    
    # 총 재생 횟수가 큰 장르부터 탐색
    for genre, nums in sum_dic:
        if genre in dic.keys():
            # 어떤 장르의 노래가 1개 밖에 없는 경우, 하나만 앨범에 수록
            if len(dic[genre]) == 1:
                answer.append(dic[genre][0][1])
            else:
                answer.append(dic[genre][0][1])
                answer.append(dic[genre][1][1])
    
    return answer
