
def solution(clothes):
    answer = 1
    dic = {}
    
    # 옷의 종류로 딕셔너리 생성
    for i in clothes:
        key = i[1]
        value = i[0]
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]
            
    # ans = ans * (종류별 + 1 ) 
    for key in dic.keys():
        answer = answer * (len(dic[key]) + 1)
        
    # ans - 1(아무것도 안입는건 없기 때문에)
    return answer - 1
