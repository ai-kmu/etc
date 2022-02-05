class Solution:
    
    #nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
    #식을 바꾸면 nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
    #즉 원래의 수와 뒤집은 수의 차이가 같으면 nice pairs가 됨
    #이 diff가 같은 수들을 count해서 nice piars의 수를 구함
    
    def countNicePairs(self, nums: List[int]) -> int:
        #숫자를 문자로 바꿔서 뒤집은 뒤 다시 숫자로 반환해주는 함수
        def rev(x):
            x = str(x)
            x = x[::-1]
            x = int(x)
            return x
        
        #diff의 count를 저장하기 위한 dict
        mydict = {}
        answer = 0
        
        #diff를 count해서 mydict에 저장
        for num in nums:
            diff = num - rev(num)
            if diff in mydict:
                mydict[diff] += 1
            else:
                mydict[diff] = 1
        
        #count한 diff의 수를 통해서 몇개의 쌍이 존재하는지 구함(조합공식)
        for count in mydict.values():
            answer += count*(count-1)//2

        return answer%(10**9+7)
                
 
