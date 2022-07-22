def solution(phone_book):
    # phone book을 sort를 통해 오름차순 정렬을 한다
    phone_book = sorted(phone_book)  
    
    # 정렬된 전화번호들을 루프를 돌며 탐색 시작
    # 현재 번호를 key로 놓고 이후에 등장하는 번호들과 비교
    for i in range(len(phone_book)-1):
        key = phone_book[i] 
        if phone_book[i+1][:len(key)] == key: return False 
        
    return True
