'''아이디어
한 종류, a 가지 = a
두 종류, a / b 가지 = (a + b) + (ab)
세 종류, a / b / c 가지 = (a + b + c) + (ab + bc + ca) + abc
==>
(x+a) = x + a -> x = 1 대입 후 1 빼줌
(x+a)(x+b) = x^2 + (a + b)x + (ab) -> x = 1 대입 후 1 빼줌
(x+a)(x+b)(x+c) = x^3 + (a + b + c)x^2 + (ab + bc + ca)x + (abc) -> x = 1 대입 후 1 빼줌

따라서 개수 + 1을 다 곱하고 1 빼주면 됨
'''

from functools import reduce
from collections import defaultdict

def solution(clothes):
    # lambda: 1 -> 기본값을 1로 해줌 (개수 + 1의 효과)
    hash_closet = defaultdict(lambda: 1)
    # 종류 별로 1 씩 더해줌
    for c in clothes:
        hash_closet[c[1]] += 1
    # 그렇게 찾은 (개수 + 1)로 리스트 만듦
    lengths = list(hash_closet.values())
    
    # length 안의 모든 요소를 곱하고 (= (x+a)(x+b) ... )
    # 1을 빼주면 답임
    return reduce(lambda x, y: x * y, lengths) - 1
