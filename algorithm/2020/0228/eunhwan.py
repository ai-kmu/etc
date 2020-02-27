def solution(words):
    char_freq = {}
    for word in words:
        cur = char_freq
        for char in word:
            try:
                cur[char]['num'] += 1
            except:
                cur[char] = {'num':1}
            cur = cur[char]  # cursor 를 마지막에 갱신

    res = 0

    for word in words:
        cur = char_freq
        for char in word:
            res += 1
            if cur[char]['num'] == 1:
                break
            else:
                cur = cur[char]
    return res
