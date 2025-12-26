class Solution:
    def reverseBits(self, n: int) -> int:
        print(bin(n))
        ans = bin(n)
        ans = ans[2:]
        print(len(ans))
        tmp = ''
        ans_revlist = list(reversed(ans))
        while len(ans_revlist) <= 31:
            ans_revlist.append('0')
        print(len(ans_revlist))
        print(ans_revlist)
        ans_list = list(reversed(ans_revlist))
        answer = 0
        for r in range(len(ans_list)):
            answer += int(ans_list[r]) * (2**r)
            # print(int(ans_list[r]) * (2**r))
        return answer
