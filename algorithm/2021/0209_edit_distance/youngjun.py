#leetcode
#72. Edit Distance
class Solution(object):
    
    #단어 간의 유사도를 평가하는 척도로 Levenshtein distance를 사용하는데 
    #Source 문자열을 insert,remove, replace을 몇번 해서 Target 문자열로 바꿀는 있는지  계산해 최소값을       
    #구하고 이를 유사도 판단의 척도로 사용함
    #밑에가 Levenshtein distnace 코드 
    def levenshtein(self,s1, s2, debug=False):
        if len(s1) < len(s2): # Target 문자열이 더 길다면 
            return self.levenshtein(s2, s1, debug)

        if len(s2) == 0: # Target 문자열이 빈칸이라면 
            return len(s1)

        previous_row = range(len(s2) + 1) # 
        for i, c1 in enumerate(s1):
            current_row = [i + 1]  # target 문자열이 empty string일 때를 가정한 비용을 추가 
            for j, c2 in enumerate(s2):
                #각 operation이 일어났을 때의 비용을 계산
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                #그 값들중 최소값을 추가 
                current_row.append(min(insertions, deletions, substitutions))

            previous_row = current_row

        return previous_row[-1]
    
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.levenshtein(word1,word2)
        
