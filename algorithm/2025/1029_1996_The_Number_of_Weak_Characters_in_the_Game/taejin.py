class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # 비교 기준 변수, 카운트 변수
        pivot = 0
        cnt = 0

        # 정렬
        properties.sort(key=lambda x: (-x[0],x[1]))

        # 현재 제일 큰놈보다 작으면 증가, 아니면 갱신 (y값 기준, 정렬되었으니)
        for x, y in properties:
            if y < pivot:
                cnt += 1
            else:
                pivot = y


        return cnt
