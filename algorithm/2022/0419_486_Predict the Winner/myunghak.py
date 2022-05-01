# 총 n 자리라 가정 하자
# 그럼 맨 앞자리는 n!마다 1씩 증가한다.
# 그 다음 자리는 (n-1)! 마다 1씩 증가한다.

# 위에서 1씩 증가한다고 했는데 무엇으로 부터 1씩 증가하는지를 찾아야한다.
# 우선 맨 앞자리는 1로부터 1씩 증가한다.
# 두번째 자리는 맨 앞자리를 제외하고 SORTING한 것에서부터 1씩 증가한다.
# 이것을 구현하기 위해 n_set이라는 변수를 만들었다.


class Solution:
    def getPermutation(self, n, k):
        n_set = [i+1 for i in range(n)]  # sorting 되어 있는 값, 여기서 하나씩 가져다 쓸 것
        ans = ""
        k-=1
        
        ch_num = [1] # 미리 팩토리얼을 계산 해 놓음(change number)
        for i in range(n-1):
            ch_num.append((i+1) * ch_num[-1])
        
        for i in range(n-1):
            ans+= str(n_set.pop(k // ch_num[-i-1])) # 몇번 바뀌어야 하는지 계산하여 그것 만큼 n_set에서 pop해줌
            k = k % ch_num[-i-1]
            
        return ans + str(n_set.pop())
