class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        i = 0
        str_lst = [""]*numRows     
        
        for letter in s:
            print(i)
            if i == numRows-1:  
                go_down = False 
            elif i == 0:        
                go_down = True # i==0일 경우 아래로 내려감
                
            str_lst[i] += letter
            i = (i+1) if go_down else i-1  					
        return "".join(str_lst)

