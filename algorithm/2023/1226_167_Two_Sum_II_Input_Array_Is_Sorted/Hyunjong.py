class Solution(object):
    def twoSum(self, numbers, target):
        # 왼쪽 포인터와 오른쪽 포인터를 초기화
        left_part, right_part = 0, len(numbers) - 1
        # 반복
        while left_part < right_part:
            # 현재 합을 계산
            current_sum = numbers[left_part] + numbers[right_part]
            # 현재 합이 목표 값과 같으면 인덱스를 반환
            if current_sum == target:
                return [left_part + 1, right_part + 1] 
            # 현재 합이 목표 값보다 작으면 왼쪽 포인터를 오른쪽으로 이동
            elif current_sum < target:
                left_part += 1
            # 현재 합이 목표 값보다 크면 오른쪽 포인터를 왼쪽으로 이동
            else:
                right_part -= 1
        # 없으면 빈 리스트를 반환
        return []
