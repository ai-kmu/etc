from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        length = len(str(n))
        
        powers = []
        
        tmp = 1
        
        while len(str(tmp)) <= length:
            if len(str(tmp)) == length:
                powers.append(tmp)
            tmp *= 2
        
        counter = Counter(str(n))
        
        return any([counter == Counter(str(x)) for x in powers])
