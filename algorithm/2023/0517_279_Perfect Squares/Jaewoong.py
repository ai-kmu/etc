class Solution:
    def numSquares(self, n: int) -> int:
        # output의 초기 값 선언
        res = 1 
        # 초기 list 선언
        # n = 12인경우, q=[12]
        q = [n]
        vis = set()
        # list의 값을 비워나갈 예정
        while q:
            print(q)
            # q의 길이만큼 반복
            q_len = len(q)
            
            for i in range(q_len): 
                # num에 값 저장시킴, num=12
                num = q[i]
                # 1~12 까지 하나씩 제곱승해서 빼봄 = square
                for j in range(1, num+1): 
                    # 현재값은 temp
                    temp = num-(j*j)
                    # 끝나면 0이되고, 아니면 1을 더해서 더할값(output)이 증가
                    if temp == 0: 
                        return res
                    # 0보다 작아지면 원하는 값이 아님
                    if temp < 0: 
                        break
                    # 중복되는 값 제거
                    # vis에 temp값이 없으면 vis와 q에 추가
                    if temp not in vis: 
                        vis.add(temp)
                        q.append(temp)
            res += 1
            # 이전 값들은 고려하지 않음
            q = q[q_len:]
        return res
