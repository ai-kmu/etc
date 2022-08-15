'''
- 최대한 2명씩 태울 수 있는 경우를 많이 만들기 위해서는 남아있는 사람 중 제일 몸무게가 작은 사람과 큰 사람이 함께 타야한다.
  1. loop를 돌면서 남아있는 사람 중 제일 몸무게가 가벼운 사람(people[i])과 제일 무거운 사람(people[j])의 몸무게 합이 limit을 넘지 않는 경우,
    --> i, j 모두 이동, cnt += 1
  2. 한 사람만 태울 수 있는 경우, 제일 무거운 사람 한 명만 태운 것임
    --> j 만 이동, cnt += 1
'''

def solution(people, limit):
    
    # 이진 탐색을 위해서 정렬
    people.sort()
    
    cnt = 0
    i, j = 0, len(people)-1
    
    # 이진 탐색
    while i <= j:
        cnt += 1
        
        if people[i] + people[j] <= limit:
            i += 1
        
        j -= 1
    
    return cnt
