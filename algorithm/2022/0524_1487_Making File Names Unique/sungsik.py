# 오답 코드
import re


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        def getLowestNum(nums):
            for i in range(len(nums.items())):
                if nums.get(i, False):
                    continue
                else:
                    return i
            return len(nums.items())

        name_map = dict()
        for i, name in enumerate(names):
            if name in name_map.keys():
                idx = getLowestNum(name_map[name])
                name_map[name][idx] = True
                if idx > 0:
                    names[i] = name + f"({idx})"
                name_map[names[i]] = {0: True}
            else:
                name_map[name] = {0: True}
                while re.match(".*\(\d+\)", name):
                    j = len(name)-1
                    while name[j] != "(":
                        j -= 1
                    prefix = name[:j]
                    suffix = name[j:]
                    
                    num = int(suffix[1:-1])
                    if num <= 0:
                        break
                    if name_map.get(prefix, dict()).get(num, False):
                        idx = getLowestNum(name_map[prefix])
                        name_map[prefix][idx] = True
                    else:
                        tmp = name_map.get(prefix, dict())
                        tmp[num] = True
                        name_map[prefix] = tmp
                    name = prefix
            print(name_map)
            
        return names
            
