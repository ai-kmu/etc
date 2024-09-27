class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(' ')
        str_list.reverse()

        output_str = ''
        str_len = len(str_list)
        for idx, elem in enumerate(str_list):
            if elem == '':
                continue

            output_str += (elem + ' ')

        return output_str[:len(output_str) - 1]
