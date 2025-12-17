# 솔루션 참고, 풀이 안 해주셔도 괜찮습니다.
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []  # 최대 개수를 우선으로 뽑기 위한 힙 (음수 사용)

        # 각 문자의 개수가 0보다 크면 힙에 추가
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        result = []  # 결과 문자열을 리스트로 관리

        while pq:
            count, ch = heapq.heappop(pq)

            # 같은 문자가 연속 3번 되는 경우 방지
            if len(result) >= 2 and result[-1] == result[-2] == ch:
                if not pq:
                    break  # 대체할 문자가 없으면 종료

                count2, ch2 = heapq.heappop(pq)
                result.append(ch2)

                # 사용한 문자 개수 감소 후 다시 힙에 삽입
                if count2 + 1 < 0:
                    heapq.heappush(pq, (count2 + 1, ch2))

                # 사용하지 못한 원래 문자를 다시 힙에 넣음
                heapq.heappush(pq, (count, ch))
            else:
                # 연속 조건에 걸리지 않으면 바로 사용
                result.append(ch)

                if count + 1 < 0:
                    heapq.heappush(pq, (count + 1, ch))

        return "".join(result)
