# 실패 이유를 모르겠음 뭐가 문제지??
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    store = dict()
    
    for i, v in enumerate(phone_book):
        store[i] = v
    
    for i in range(len(store)):
        tmp = store.pop(i)
        va = list(store.values())
        for j in range(len(store)):
            if tmp in va[j]:
                return False
    return True

# 오래 걸림 => 효율성 실패
# 원인 분석 => store.values로 해서 찾으면 리스트에서 찾는 것과 동일한 시간이 걸려서 그런듯
def solution(phone_book):
    store = {}
    
    for i in range(len(phone_book)):
        store[i] = phone_book[i]

    
    for i in range(len(phone_book)):
        current = store[i]
        tmp = ''
        for j in current:
            tmp = tmp + j
            if tmp in store.values() and tmp != current:
                return False
    return True
## 통과
# 값을 key에 집어넣고 키 값에서 바로 찾으니 통과됨
def solution(phone_book):
    store = {}
    
    for i in range(len(phone_book)):
        store[phone_book[i]] = i

    for num in phone_book:
        tmp = ''
        for j in num:
            tmp = tmp + j
            if tmp in store and tmp != num:
                return False
    return True
