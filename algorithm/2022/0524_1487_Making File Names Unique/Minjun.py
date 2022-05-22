class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        file = {}
        for name in names:
            if name not in file:
                file[name] = 1
            k = 0;
            
            while file[name] not in file:
                k += 1
                file[name] = file[name].keys() + '(' + str(k) + ')'
        
        return file.keys()
                
