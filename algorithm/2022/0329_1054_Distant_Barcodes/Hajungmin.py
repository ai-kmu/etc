from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Counter함수를 사용해서 바코드의 숫자들의 개수를 센다.
        count = Counter(barcodes)
        # 바코드의 숫자와 개수를 담을 리스트를 만든다.
        nums = []
        
        # count에 담긴 key와 value를 리스트에 담는다.
        for k, v in count.items():
            nums.append([k,v])
        i = 0
        
        # 결과를 저장할 리스트를 생성한다.
        result = [0] * len(barcodes)
        
        # 바코드의 숫자와 개수가 담긴 리스트를 개수를 기준으로 
        # 작은 개수를 갖는 숫자가 앞으로 옫도록 정렬한다.
        nums = sorted(nums,key = lambda v:v[1])
        
        # 인덱스가 결과와 길이가 같아질 때까지 반복을 돌며
        # index 0번부터 개수가 많은 숫자를 result에 넣는다.
        # ex. 만약 1이 많은 개수를 갖고 있다면 다음과 같이 채워짐
        # result = [1, 0, 0, 0, 0, 0] -> [1, 0, 1, 0, 0, 0] ...
        # 사용한 숫자는 pop을 사용해 없애준다.
        
        while i <len(result):
            result[i] = nums[-1][0]
            nums[-1][1] -= 1
            if nums[-1][1] == 0:
                nums.pop()
            i+=2
        # i를 1로 만들어서 1부터 다시 반복을 돈다.
        
        i=1
        
        # 이후에 남은 숫자들을 다시 반복을 통해 빈 공간에 넣어준다.
        while i <len(result):
            result[i] = nums[-1][0]
            nums[-1][1] -= 1
            if nums[-1][1] == 0:
                nums.pop()
            i+=2
            
        return result
