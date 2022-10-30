class Solution:
    def ladderLength(self, bw: str, ew: str, wordList: List[str]) -> int:
        # 탐색을 빠르게 하기 위한 set 지정
        word_set = set(wordList)

        # 예외처리: 끝 단어가 word_set에 없으면 도달 불가
        if ew not in word_set:
            return 0
        word_set.remove(ew)

        n = len(bw)
        step = 0

        # 시작: 양방향에서 왔다갔다 할 거임
        front = {bw}
        reverse = {ew}
        # 둘 다 있을 때
        while reverse and front:
            # 스텝 이동
            step += 1
            new_set = set()
            # 짧은 쪽에서만 이동
            if len(front) > len(reverse):
                front, reverse = reverse, front
            for word in front:
                # 각 단어들의 다음 스텝 모두 지정
                cands = {word[:i] + t + word[i+1:]
                         for t in 'qwertyuiopasdfghjklzxcvbnm'
                         for i in range(n)}
                for cand in cands:
                    # 그게 reverse면 거기서 끝
                    if cand in reverse:
                        return step + 1
                    # 쓸 수 없는 애는 제거
                    if cand not in word_set:
                        continue
                    # 한 번 쓴 애는 제거하고 새로 front에 넣음
                    word_set.remove(cand)
                    new_set.add(cand)
            front = new_set
        return 0
