# 솔루션 참고

class Solution:
    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
        # row와 column의 합이 같으면 같은 대각선에 속함을 이용
        d = defaultdict(list)

        for i in range(len(A)):
            for j in range(len(A[i])):
                # 합을 키로 값을 더해줌
                d[i+j].append(A[i][j])

        # 딕셔너리에 더했던 순서와 대각선 방향이 원하는 순서가 다름
        # 이에 맞춰 리스트에 다시 담아준 후 반환
        return [v for k in d.keys() for v in reversed(d[k])]
