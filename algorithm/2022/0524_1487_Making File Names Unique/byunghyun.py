# 오답
# TLE
class Solution:
    def get_unique_name(self, names, entire_index):
        # 넘버링은 0부터 시작한다.
        numbering = 0
        while True:
            numbering += 1
            new_name = names[entire_index] + '(' + str(numbering) + ')'
            result = new_name in names[:entire_index]
            if result is False:
                break
        return new_name
    
    def getFolderNames(self, names: List[str]) -> List[str]:
        # 이중 반복문을 이용해 중복되는 문자열이 있는지 검사한다.
        for entire_index in range(1, len(names)):
            for local_index in range(entire_index):
                # 만약 중복되는 문자열이 존재한다면
                if names[entire_index] == names[local_index]:
                    # 넘버링을 붙인 새로운 문자열을 생성한다.
                    new_name = self.get_unique_name(names, entire_index)
                    # 새로운 문자열을 사용하게 된다.
                    names[entire_index] = new_name
        return names
                    
