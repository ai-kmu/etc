from collections import Counter

def solution(clothes):
    # 마지막에 곱셈을 하기 위해서 answer를 1로! 
    answer = 1
    clothes_type = []
    # clothes_type 리스트에 type 넣기
    for type in clothes:
        clothes_type.append(type[1])
        
    # Counter 사용해서 clothes_type 별로 몇개 있는지 dict형태로 저장    
    clothes_count = dict(Counter(clothes_type))
    
    # value 값 뽑기 위해서 items 뽑은걸 key, value로 받아주고
    for key, value in clothes_count.items():
        # value 값들 뽑은거 곱하고 1씩 더하기
        answer *= value + 1
    # 마지막에 answer에서 1 뻬기
    return answer - 1
