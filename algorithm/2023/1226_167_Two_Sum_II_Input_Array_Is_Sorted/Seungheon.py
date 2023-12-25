class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # dictionary에 값을 key, index를 value로 저장
        num_dict = {}
        for i, num in  enumerate(numbers):
            num_dict[num] = i
            
        # target - num이 dictoinary에 존재하면 return
        for i, num in enumerate(numbers):
            difference = target - num
            if difference in num_dict and num_dict[difference] != i:
                return [i+1, num_dict[difference]+1]
