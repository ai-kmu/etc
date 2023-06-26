class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 애너그램 그룹을 저장할 해시맵 생성
        anagram_groups = {}  
        for word in strs:
            # 단어를 정렬하여 애너그램을 동일한 형태로 만듦
            sorted_word = ''.join(sorted(word))  
            # 정렬된 단어가 이미 해시맵에 키로 존재하는 경우
            if sorted_word in anagram_groups:  
                # 해당 키에 단어를 추가
                anagram_groups[sorted_word].append(word)  
            else:
                # 새로운 키로 단어 리스트를 생성하여 해시맵에 추가
                anagram_groups[sorted_word] = [word]  
        # 애너그램 그룹들의 리스트 반환
        return list(anagram_groups.values())  
