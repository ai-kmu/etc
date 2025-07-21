class Solution:
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        
        result = []
        idx = 0

        while i >= 0 or j >= 0 or idx: 
            if i >= 0:
                bin_a = int(a[i])
            else:
                0 
                
            if j >= 0:
                bin_b = int(b[j])
            else:
                0 

            total = bin_a + bin_b + idx 

            result.append(str(total % 2))
            idx = total // 2 
            i -= 1 
            j -= 1 
        
        return "".join(reversed(result))
