class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dic={} 
        for word in strs:
            temp_key=tuple(sorted(list(word))) #알파벳 하나하나 분리해서 정렬
            try:
                word_dic[temp_key].append(word) #만약 이미 딕셔너리에 있으면 append

            except:
                word_dic[temp_key]=[word] #없으면 key, value 생성

        answers=[] #최종 리턴할 answer 배열

        for val in word_dic.values(): 
            answers.append(val)
        return answers