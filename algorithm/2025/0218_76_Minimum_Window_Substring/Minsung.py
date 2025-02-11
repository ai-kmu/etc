from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = defaultdict(int)  # t에 있는 문자 종류와 수 저장
        for c in t:
            target[c] += 1
        
        # t에 있는 문자가 있는 위치와 종류 저장
        index_alpha = [[0, '#']]  # 이후 연산에서, 아무것도 선택하지 않는 경우를 위해 삽입
        for i, c in enumerate(s):
            if target[c] != 0:
                index_alpha.append([i,c])
        # [(0, 'A'), (3, 'B'), (5, 'C'), (9, 'B'), (10, 'A'), (12, 'C')]

        # 각 위치별로 포함한 문자의 누적 종류 저장 
        for i in range(len(index_alpha)):
            if i == 0: 
                tmp = defaultdict(int)
                tmp[index_alpha[i][1]] = 1
                index_alpha[i][1] = tmp
            else:
                tmp = defaultdict(int)
                tmp[index_alpha[i][1]] = 1
                for k, v in index_alpha[i-1][1].items():
                    tmp[k] += v
                index_alpha[i][1] = tmp
        # [[0, defaultdict(<class 'int'>, {'#': 1})], [0, defaultdict(<class 'int'>, {'A': 1, '#': 1})], [3, defaultdict(<class 'int'>, {'B': 1, 'A': 1, '#': 1})], [5, defaultdict(<class 'int'>, {'C': 1, 'B': 1, 'A': 1, '#': 1})], [9, defaultdict(<class 'int'>, {'B': 2, 'C': 1, 'A': 1, '#': 1})], [10, defaultdict(<class 'int'>, {'A': 2, 'B': 2, 'C': 1, '#': 1})], [12, defaultdict(<class 'int'>, {'C': 2, 'A': 2, 'B': 2, '#': 1})]]

        # 정답을 도출할 수 없는 경우 empty return
        if len(index_alpha)==0 or not self.match(index_alpha[-1][1], target): 
            return ''

        margin = int(1e5)  # 가장 작은 substring 측정을 위한 변수
        ans_left, ans_right = index_alpha[0][0], index_alpha[0][0]

        for i in range(len(index_alpha)):
            if not self.match(index_alpha[i][1], target):  # 현재 i로 정답을 도출할 수 없을 경우 skip
                continue
            
            # binary search를 이용하여, 현 위치에서 만들 수 있는 가장 작은 substring 탐색
            left, right = 0, i-1
            while left <= right:
                mid = (left+right) // 2
                # mid 위치와 현 위치 사이의 substring이 포함한 문자 종류 측정
                tmp = defaultdict(int)
                for k, v in index_alpha[i][1].items():
                    tmp[k] = v - index_alpha[mid][1][k]
                if self.match(tmp, target):  # substring을 만들 수 있다면, minimal인지 측정
                    left = mid + 1
                    if margin > index_alpha[i][0] - index_alpha[mid+1][0]:
                        margin = index_alpha[i][0] - index_alpha[mid+1][0]
                        ans_left = index_alpha[mid+1][0]
                        ans_right = index_alpha[i][0]
                else:
                    right = mid - 1

        return s[ans_left:ans_right+1]

    def match(self, source: defaultdict, target: defaultdict):
        for k, v in target.items():
            if source[k] >= v: 
                pass
            else: 
                return False
        return True
