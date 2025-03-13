class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        word = ''
        for i in digits:
            word += str(i)
        word_int = int(word) + 1
        answer = []
        for i in str(word_int):
            answer.append(int(i))
            
        return answer
