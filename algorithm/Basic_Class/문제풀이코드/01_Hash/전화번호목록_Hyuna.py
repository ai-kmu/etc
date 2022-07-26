from collections import defaultdict
def solution(phone_book):
    answer = True
    dict=defaultdict(list)
    
    # 전화번호의 길이를 키값으로 딕셔너리를 만들어준다
    for num in phone_book:
        dict[len(num)].append(num)
        
    
    for num in phone_book:
        # 전화번호보다 작은 길이를 가진 번호들을 조회한다
        for i in range(1,len(num)):
            for item in dict[i]:
                # 조회하는 번호들이 전화번호의 앞부분과 같다면 False를 반환한다
                if num[0:i] == item :
                    return False
    
    return answer    
   
