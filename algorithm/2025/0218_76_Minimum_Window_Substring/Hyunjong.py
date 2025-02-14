# 못풀어서 답지 봤습니다... 리뷰 안해주셔도 됩니다

class Solution:
    def minWindow(self, s, t):
        m = len(s)
        n = len(t)

        t_freq = Counter(t)

        st = []
        for i in range(m):
            if s[i] in t_freq:
                st.append(i)

        result = ""
        count = 0
        freq = defaultdict(int)
        min_len = float('inf')
        left = 0
        for right in range(len(st)):
            c = s[st[right]]
            freq[c] += 1
            if freq[c] <= t_freq[c]:
                count += 1

            if count == n:
                # move left
                c = s[st[left]]
                while freq[c] > t_freq[c]:
                    freq[c] -= 1
                    left += 1
                    c = s[st[left]]

                if st[right] - st[left] + 1 < min_len:
                    min_len = st[right] - st[left] + 1
                    result = s[st[left]:st[right] + 1]

        return result
