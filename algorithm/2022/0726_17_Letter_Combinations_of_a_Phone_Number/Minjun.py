class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit = {}
        ascii_a = 97
        answer = []
        for i in range(2, 10):
            if i == 7 or i == 9:
                digit[i] = [chr(ascii_a), chr(ascii_a+1), chr(ascii_a+2), chr(ascii_a+3)]
                ascii_a += 4
                continue
            
            digit[i] = [chr(ascii_a), chr(ascii_a+1), chr(ascii_a+2)]
            ascii_a += 3
        
        def combi(digit_list, tmp):
            for i in range(len(digit_list)):
                for j in range(len(tmp)):
                    tmp.append(digit_list[i] + tmp[j])
        
        
        tmp = []
        nums = list(digits)

        if len(digits) == 0:
            return
        
        for i in nums:
            combi(digit[int(i)], tmp)
        print(tmp)

                
                

