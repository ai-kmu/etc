class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = {}
        output = []
        for i in names:
            if i not in used:
                used[i] = 1
                output.append(i)
            else:
                k = used[i]
                used[i] += 1
                new = i + "(" + str(k) + ")"
                while new in used:
                    k += 1
                    new = i + "(" + str(k) + ")"
                    used[new] = 1
                    output.append(new)
        return(output)
    
#메모리 초과
