from itertools import permutations
import math

# 소수 찾는 공식을 함수화함
def is_prime_number(x):
    # 2보다 작으면 False
    if x < 2:
        return False
    # 2부터 x의 제곱근까지 순회하면서
    for i in range(2, int(math.sqrt(x)) + 1):
        # 나누어 떨어지면 False
        if x % i == 0:
            return False
    # 그렇지 않으면 True를 반환한다.
    return True

def solution(numbers):
    answer = 0
    nums = [n for n in numbers]
    per = []
    # 숫자들을 뽑아서 만들 수 있는 수를 permutations를 이용해 구해준다.
    for i in range(1, len(numbers) + 1):
        per += list(permutations(nums, i))
    # 중복이 있을 수 있어 set을 사용한다.
    new_nums = list(set([int(("").join(p)) for p in per]))
    
    # 위에서 만든 소수 찾는 함수를 이용하여, answer를 구한다.
    for n in new_nums:
        if is_prime_number(n):
            answer += 1
            
    return answer
