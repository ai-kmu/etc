from collections import Counter
class Solution: 
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(numbers):
            list_rev = [] #거꾸로 넣기 위한 빈 리스트 생성
            numbers_to_rev = str(numbers) #거꾸로 하는 숫자를 문자열로 만든뒤 하나씩 거꾸로 넣는 작업 수행
            for i in range (len(numbers_to_rev)-1, -1, -1):
                list_rev.append(numbers_to_rev[i]) #거꾸로 넣었다. 
        #거꾸로 넣었지만 따로따로 들어갔기 때문에 빈문자열을 만들어 하나씩 넣어서 합친다. 
            revolve = ''
            for num in list_rev:
                revolve += num  
            return int(revolve) #거꾸로 된 문자열에 int로 만들어서 거꾸로 된 숫자 내보내기 
        
        #a + rev(b) = b + rev(a)의 의미는 a - rev(a) = b - rev(b)의 의미다.
        #리스트안에서 숫자와 숫자를 거꾸로 한 값의 차이가 같은 짝의 개수를 세면 된다. 
        
        sub_list = []                
        for num in nums:
            sub_list.append(num - rev(num))
        
        sub_count = Counter(sub_list) #Counter을 이용하여 숫자간의 차이에 따른 원소의 개수를 딕셔너리로 담았다. 
        
        count = 0
        for sub_values in sub_count.values(): #values()를 이용해 딕셔너리에서 value를 꺼내기 
        # nC2만큼 answer에 더해준다.(조합공식), 어차피 value가 1개만 있으면 0이  count에 누적되지 않는다.  
            count += sub_values * (sub_values-1) // 2
        
        return count % 1000000007 #너무 많은 pair을 대비하여 큰 수로 나눴다. 
