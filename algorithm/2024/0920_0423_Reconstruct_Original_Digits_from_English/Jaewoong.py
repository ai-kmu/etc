class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = []
        for i in s:
            word_list.append(i)
        
        word = ''
        all_word = []

        if word_list[-1] != ' ':
            word_list.append(' ')
        
        for i in word_list:
            if i != ' ':
                word += i
            elif i == ' ':
                all_word.append(word)
                word = ''
        ans = ''

        reverse_all_word = list(reversed(all_word))
        reverse_all_word_removed = []
        for i in reverse_all_word:
            if i != '':
                reverse_all_word_removed.append(i)

        for i in range(len(reverse_all_word_removed)):
            if i != len(reverse_all_word_removed) - 1:
                ans += reverse_all_word_removed[i]
                ans += ' '
            else:
                ans += reverse_all_word_removed[i]
        
        return ans
            
        

            
