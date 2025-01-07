class Solution:
    def printVertically(self, s: str) -> List[str]:
        string_list = s.split(" ")
        idx = 0
        result = []

        max_num = 0

        for i in string_list:
            max_num = max(len(i), max_num)

        while idx < max_num:
            s = ""
            for string in string_list:
                if len(string) > idx:
                    s += string[idx]
                else:
                    s += " "
            result.append(s)
            
            idx += 1
            
        for ii, i in enumerate(result):
            if i[-1] == ' ':
                result[ii] = i.rstrip()

        return result
