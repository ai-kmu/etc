from collections import Counter

def solution(str1, str2):
    answer = 0
    
    list_1 = []
    list_2 = []
            
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 두 글자씩 끊기
    for i in range(len(str1)-1):
        tmp = str1[i] + str1[i+1]
        # 문자가 아닌 경우는 제외
        if tmp.isalpha():
            list_1.append(tmp)
    
    for i in range(len(str2)-1):
        tmp = str2[i] + str2[i+1]
        if tmp.isalpha():
            list_2.append(tmp)
    
    # Counter 써서 딕셔너리 형태로 바꿔줌
    multiset_1 = Counter(list_1)
    multiset_2 = Counter(list_2)
    
    same = []
    total = []
    
    # 교집합 구하기
    for m1 in multiset_1.keys():
        # 만약 현재 key가 multiset_2 딕셔너리에 존재한다면
        if m1 in multiset_2.keys():
            # multiset_2에 동일한 key의 개수가 더 많은 경우
            if multiset_1[m1] < multiset_2[m1]:
                # 더 작은 개수를 tmp로 지정
                tmp = multiset_1[m1]
            
            # multiset_1에 동일한 key의 개수가 더 많은 경우
            else:
                tmp = multiset_2[m1]
                
            same += [m1] * tmp
    
    # 합집합 구하기
    total = list_1
    
    for m2 in multiset_2.keys():
        # 현재 key가 multiset_1의 키값에 존재하지 않는다면
        if m2 not in multiset_1.keys():
            total += multiset_2[m2] * [m2]
            
        # 현재 key가 multiset_1의 키값에 존재한다면
        if m2 in multiset_1.keys():
            if multiset_2[m2] > multiset_1[m2]:
                total += [m2] * (multiset_2[m2] - multiset_1[m2])
    
    try:      
        # 자카드 유사도 계산
        J = len(same) / len(total)
        answer = J * 65536
        answer = int(answer)
    
        return answer
    
    # total이 0이 되는 경우는 65536 출력
    except:
        return 65536
