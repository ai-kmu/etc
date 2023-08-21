from itertools import product
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # 사용할 영단어 정의
        letter = ['a', 'b', 'c']
        
        # product를 통해 조합 만듬
        permute = list(product(letter, repeat = n))
        permute = [''.join(i) for i in permute]
        # abb와 같이 중복되는 부분 저장하는 리스트인 del_list 정의
        del_list = []
        for j in permute:
            for l in range(len(j) - 1):
                if j[l] == j[l+1]:
                    del_list.append(j)
        # 두 리스트끼리 set을 통해 빼서 중복되는 부분 제거
        permute = set(permute) - set(del_list)
        # 정렬
        permute = sorted(list(permute))
        
        if k <= len(permute):
            return permute[k-1]
        else:
            return ""
