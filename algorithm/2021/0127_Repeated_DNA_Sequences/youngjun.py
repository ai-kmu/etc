class Solution(object):
    def findRepeatedDnaSequences(self, s):
        ans,checked = set(),set() # 중복값 허용안하기 때문에 set 사용
      
        for i in range(len(s) - 9): # 뒤에 마지막 10자리가 남을 때까지 반복하면서 
            sequence = s[i:i + 10]
            if sequence in checked: # seen안에 현재 반복된 길이 10의 substring이 존재한다면  
                ans.add(sequence) # answ에 추가 
            checked.add(sequence) #아니면 새로 seen에 추가 

        return list(ans) # ans를 list형태로 반환 
        
