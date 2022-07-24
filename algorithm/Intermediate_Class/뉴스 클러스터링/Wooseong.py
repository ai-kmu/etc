import copy

def solution(str1, str2):
    # 대소문자 무시 - 모두 소문자로
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 각 str을 다중 집합으로 만들기 - 알파벳쌍만 가능
    # -> .isalpha()는 str가 모두 알파벳일 때만 True
    set1 = []
    for i in range(len(str1) - 1):
        temp = str1[i:i+2]
        if temp.isalpha():
            set1.append(temp)
    
    set2 = []
    for i in range(len(str2) - 1):
        temp = str2[i:i+2]
        if temp.isalpha():
            set2.append(temp)
    
    # 두 집합이 모두 공집합일 경우는 1로 정의
    if (not set1) and (not set2):
        return 65536
    
    # 교집합과 합집합
    # 겹친 게 나올 경우
    # 교집합에는 적은 개수만큼, 합집합에는 많은 개수만큼 넣음
    # 안 겹치면 합집합에만 넣음
    set1_copy = copy.deepcopy(set1)
    set2_copy = copy.deepcopy(set2)
    inter = []
    union = []
    # 둘 중 하나 다 떨어짐 = 겹칠 수 없음
    while set1_copy and set2_copy:
        elem = set1_copy.pop()
        if elem in set2_copy:
            # set1은 이미 하나 pop 해서 +1로 보정
            in_set1 = set1_copy.count(elem) + 1
            in_set2 = set2_copy.count(elem)
            
            # 교집합엔 적은 개수만큼
            inter += [elem] * min(in_set1, in_set2)
            # 합집합엔 많은 개수만큼
            union += [elem] * max(in_set1, in_set2)
            
            # 넣은 거 빼기
            set1_copy = [i for i in set1_copy if i != elem]
            set2_copy = [i for i in set2_copy if i != elem]
        
        # 안 겹치는 건 union에만 넣음
        else:
            union.append(elem)
    
    # 합집합에 남은 거 더 해주기 (둘 중 하나는 빈 리스트)
    union += set1_copy + set2_copy
    # print("교", inter)
    # print("합", union)
        
    return ((len(inter) / len(union)) * 655360) // 10
