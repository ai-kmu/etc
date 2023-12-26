class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer 방식으로 풀이
        start = 0  # 시작 인덱스
        end = len(numbers) - 1  # 끝 인덱스: 맨 오른쪽부터 거꾸로 시작

        # start 인덱스가 end 인덱스보다 작을동안 while문 반복
        while start < end:
            # 두 수의 합이 target보다 크면 end를 -1
            if numbers[start] + numbers[end] > target:
                end -= 1
            # 두 수의 합이 target보다 작으면 start를 +1
            elif numbers[start] + numbers[end] < target:
                start += 1
            # 그 외에는 합이 target이랑 같으므로 정답 return
            # 정답 return할 때는 인덱스가 1부터 시작하므로 start와 end에 각각 +1해서 리턴
            else:
                return [start + 1, end + 1]
