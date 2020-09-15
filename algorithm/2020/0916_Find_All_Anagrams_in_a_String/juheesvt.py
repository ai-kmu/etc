class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        target_len = len(p)
        string_len = len(s)

        # 주어 문자를 ascii code로 이루어진 list
        target_set = [ord(p_) for p_ in p]
        target_set.sort()
        # 비교할 문자를 꺼낼 문자열은 ascii code로 이루어진 list
        string_set = [ord(s_) for s_ in s]

        result = list()

        for i in range(string_len):
            try:
                temp = string_set[i:i + target_len]
                temp.sort()
            except:
                break

            if len(temp) == len(target_set):
                if temp == target_set:
                    result.append(i)

        return result

