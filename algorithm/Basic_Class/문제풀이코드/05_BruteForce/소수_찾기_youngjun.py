from itertools import permutations
import math

def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = [n for n in numbers]
    per = []
    for i in range(1, len(numbers) + 1):
        per += list(permutations(nums, i))
    new_nums = list(set([int(("").join(p)) for p in per]))
    
    for n in new_nums:
        if is_prime_number(n):
            answer += 1
            
    return answer
