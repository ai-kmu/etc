def solution(phone_book):
    # 전화번호를 오름차순 정렬하면 접두사가 바로 앞에 오게 됨
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        # 접두사 부분까지의 phone_book이 앞과 뒤가 일치하면 False return
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
          return False
    # 루프를 다 돌때까지 접두사가 발견되지 않았으면 True return
    return True
    
