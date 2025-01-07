class Solution:
    def printVertically(self, s: str) -> List[str]:
        splitted_list = s.split()

        max_len = -1
        for idx in range(len(splitted_list)):
            current_len = len(splitted_list[idx])
            if current_len > max_len:
                max_len = current_len

        final_list = []
        for current_idx in range(max_len):
            current_str = ""
            for splitted_idx in range(len(splitted_list)):
                try:
                    current_ch = splitted_list[splitted_idx][current_idx]
                    current_str += current_ch
                except:
                    current_str += " "

            # splitted_second = current_str.split()
            # print(splitted_second)
            for idx in range(len(current_str) - 1, -1, -1):
                # print(idx)
                if current_str[idx] == " ":
                    current_str = current_str[:idx]
                else:
                    break

            final_list.append(current_str)

        return final_list
        
