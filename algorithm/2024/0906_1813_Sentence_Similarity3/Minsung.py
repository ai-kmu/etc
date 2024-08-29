class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        word1 = sentence1.split(' ')
        word2 = sentence2.split(' ')

        if word1 == word2:
            return True

        if len(word1) > len(word2):
            longer = word1
            shorter = word2
        else:
            longer = word2
            shorter = word1

        longer_left_index = 0
        longer_right_index = len(longer)-1
        shorter_left_index = 0
        shorter_right_index = len(shorter)-1
        
        try:
            while longer[longer_left_index] == shorter[shorter_left_index]:
                longer_left_index += 1
                shorter_left_index += 1
        except IndexError:
            pass
        
        try:
            while longer[longer_right_index] == shorter[shorter_right_index]:
                longer_right_index -= 1
                shorter_right_index -= 1
        except IndexError:
            pass

        return True if shorter_left_index > shorter_right_index else False
