# % 줘야되는 부분이 막혀서 정답보고 공부했습니다...
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 중복 제거
        deadend = set(deadends)
        # 시작 지점
        v = set('0000')
        dq = deque([('0000', 0)])

        while dq:
            now_num, ans = dq.popleft()
            # 조건 만족했을때
            if now_num == target:
                return ans
            # deadends에 있는거 걸렸을 때
            elif now_num in deadend:
                continue
            # 자물쇠 4자리이므로
            # 하나씩 변경(bfs)
            for i in range(4):
                digit = int(now_num[i])
                for move in [-1,1]:
                    # 움직였을때 현 값을 표현해주기 위해 10을 나눔
                    # (0 - 1) % 9 는 나머지가 9
                    newdigit = (digit + move) % 10 # 9가 됬다고 가정하면
                    # i가 1이면
                    newslot = now_num[:i] + str(newdigit) + now_num[i+1:] # newslot = 0 + '9' + 00
                    # 방문처리
                    if newslot not in v:
                        v.add(newslot)
                        dq.append((newslot, ans+1))
        return -1
