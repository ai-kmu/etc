from collections import defaultdict

def solution(clothes):
    dict = defaultdict(int)
    answer = 1
    
    # 해당하는 의상의 종류의 수를 늘려준다
    for item in clothes:
        dict[item[1]] += 1
    
    # 해당 옷이 조합에 포함 되지 않을 경우를 고려해서 +1을 해준다
    for key in dict:
        answer *= dict[key] + 1
    
    # 조합에는 모든 옷들이 포함되지 않은 경우가 존재하기 때문에 1을 빼준다
    return answer - 1
