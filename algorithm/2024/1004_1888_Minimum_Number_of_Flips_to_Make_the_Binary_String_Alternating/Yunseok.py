# 풀이 실패

class Solution:
    def minFlips(self, s: str) -> int:
        odd_list = s[::2]
        even_list = s[1::2]

        elem_matrix = [[even_list.count('0'), even_list.count('1')], [odd_list.count('0'), odd_list.count('1')]]
        
        # matrix의 대각 성분(좌대각, 우대각)만 남기고 모두 제거
        # 대각성분을 제거하는 과정에서 필요한 연산 횟수 구하기

        # Type-1 케이스를 반영하지 못함
        # 문제 똑바로 읽자...
