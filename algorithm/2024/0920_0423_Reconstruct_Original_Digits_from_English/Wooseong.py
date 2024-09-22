from collections import Counter

'''
**guaranteed to be valid** 조건이 있기 떄문에
일단 고유한 문자 세서 숫자 세 놓고, 나머지는 빼면서 세면 됨
고유한 거 -> (z, 0), (w, 2), (u, 4), (x, 6), (g, 8)
두 개 겹치는 거 -> (h, (3, 8)), (f, (5, 4)), (s, (7, 6))
네 개 겹치는 거 -> (o, (1, 0, 2, 4)), (i, (9, 5, 6, 8))
ex1)
owoztneoer -> zero one two
1. z, w가 하나 씩 있으니까 0, 2는 무조건 하나 있음
2. h, f, s는 없으니까 패스
3. o는 총 세 개 있는데, 이 중 두 개는 0, 2에 쓰이니까 1은 한 개임
'''
class Solution:
    def originalDigits(self, s: str) -> str:
        num_str = Counter(s)
        
        # 각 숫자에 해당하는 문자가 몇 번 씩 나왔는지 세는 리스트
        cnt = [0 for _ in range(10)]
        
        # 각 숫자마다 고유한 문자 세기
        # - 'z'가 하나 있으면 'ero'도 각각 하나 씩 무조건 있어서 셀 필요 없음
        # - guaranteed to be valid 조건
        cnt[0] = num_str['z']
        cnt[2] = num_str['w']
        cnt[4] = num_str['u']
        cnt[6] = num_str['x']
        cnt[8] = num_str['g']
        
        # 여러 곳에서 나오는 거 세기
        # 이미 셌던 0, 2, 4, 6, 8은 개수 고정이니까
        # 다른 애들은 그거 기반으로 뺴주면 됨
        # 1. 두 곳에서 나오는 거
        cnt[3] = num_str['h'] - cnt[8]
        cnt[5] = num_str['f'] - cnt[4]
        cnt[7] = num_str['s'] - cnt[6]
        
        # 2. 더 많은 곳에서 나오는 거
        cnt[1] = num_str['o'] - cnt[0] - cnt[2] - cnt[4]
        cnt[9] = num_str['i'] - cnt[5] - cnt[6] - cnt[8]
        
        # 정답은 숫자로
        return ''.join(str(i) * cnt[i] for i in range(10))
