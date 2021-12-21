class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i=0 # string index
        j=0 # pattern index
        star_index = -1 # * 위치 기억
        sen_index = 0 # * 나온 순간 s의 index 기억
        while i<len(s):
            # s와 p가 같거나 p가 ?인 경우에는 동시에 다음 문자로 넘어감
            if (j < len(p)) and ((s[i] == p[j]) or (p[j] == "?")):
                i+=1
                j+=1
            # p가 *인 경우 그 때의 p에서 index값과 s에서의 index값 저장
            elif (j < len(p)) and (p[j] == "*"):
                star_index = j
                sen_index = i
                j+=1
                
            # *을 전에 읽었을 경우 p는 * 다음 문자로, s는 *가 나왔을 때의 문자의 다음 문자로 넘어감
            elif star_index != -1:
                j = star_index + 1
                sen_index+=1
                i=sen_index
                
            else: # 위 3가지 모두 안되는 경우 false 출력
                return False

        return list(p[j:]).count('*') == len(p[j:]) # s에서 문자 다 읽은 후 p에서 남은 문자들에서의 * 개수와 남은 문자의 총 길이가 같으면 True 출력
