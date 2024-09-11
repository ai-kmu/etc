class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a = sentence1.split()
        b = sentence2.split()
        c = -2
        if len(a) > len(b):
            big = a
            small = b
        else:
            big = b
            small = a

        if small[-1] != big[-1] and small[0] != big[0]:
            return False
        if len(small) == len(big):
            for i in range(len(small)):
                if small[i] != big[i]:
                    return False
            return True

        if small[0] != big[0]:
            idx = -1
            for i in range(len(small)):
                if small[idx] != big[idx]:
                    return False
                if -idx == len(small):
                    break
                idx -= 1
                
        if small[-1] != big[-1]:
            for i in range(len(small)):
                if small[i] != big[i]:
                    return False
        
        if small[0] == big[0] and small[-1] == big[-1]:
            prefix = 0
            for i in range(len(small)):
                if small[i] != big[i]:
                    prefix = i
                    break
            small = small[prefix:]
            big = big[prefix:]
            idx = -1
            for i in range(len(small)):
                print(small, big)
                if -idx == len(small):
                    break
                if small[idx] != big[idx]:
                    return False
                idx -= 1
        return True
