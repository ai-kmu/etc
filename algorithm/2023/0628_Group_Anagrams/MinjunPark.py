class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = dict()

        for i in strs:

            si = "".join(sorted(i)) # elements는 동일하지만 다른 order의 str을 동일하게 취급하기 위한 정렬
            try:
                answer[si].append(i) 
            except:
                answer[si] = [i] # keyError시 key값에 해당하는 값 생성
                
        return answer.values()
