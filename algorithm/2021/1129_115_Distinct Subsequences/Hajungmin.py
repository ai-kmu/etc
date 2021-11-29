class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len = len(s)
        t_len = len(t)
        # 결과를 출력할 리스트를 선언해줍니다.
        result = [1]+[0]*t_len
        # s의 길이만큼 돌며 t와 비교하여 가능한 단어조합을 셉니다.
        for i in range (1, s_len+1):
            # 현재까지 몇가지의 경우의 수가 있는지 담아두는 curr를 선언합니다.
            curr = [1]
            for j in range(1, t_len+1):
                # 만약 현재 s와 t가 같다면 curr에는 이전까지의 경우의 수인 result[j]와 현재 결과값인result[j-1]를 더해준 것을 append합니다.
                if s[i-1] == t[j-1]:
                    curr.append(result[j]+result[j-1])
                # 만약 글자가 같지 않다면 그냥 현재 index의 result 값만 추가해줍니다.
                else:curr.append(result[j])
            # 최종적으로 한 루프를 돈 후 curr값을 result에 넣어줍니다.
            result = curr
        # 최종적으로 나온 가지수는 result 리스트의 가장 마지막에 있는 값이 됩니다.
        return result[-1]
