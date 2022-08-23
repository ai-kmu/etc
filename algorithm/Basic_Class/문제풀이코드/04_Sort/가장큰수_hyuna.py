def solution(numbers):
    answer = ''
    
    # numbers 리스트를 스트링 리스트로 바꿔준다
    numbers = list(map(str, numbers))
    # 가장 큰 수를 찾기 위해 여러 번 반복한 형태로 sorting을 해준다 
    # ex) 34일때 343434 30일때 303030
    numbers.sort(key= lambda x: x*3, reverse=True)
    
    # sorting 된 리스트를 스트링으로 이어준다
    answer = ''.join(numbers)
    
    # 0만 여러개 나왔을 경우 '0000'이 아닌 '0'이 출력될 수 있도록 처리   
    return '0' if not int(answer) else answer 
