# prefix 허프만 코드 문제 greedy algorithm
class Trie:
    def __init__(self):
        # value는 단어의 개수
        self.value = 0
        # key: char, value : Trie object
        self.children = {}


def solution(words):
    answer = 0
    tree = Trie()
    for word in words:
        subTrie = tree
        for i, char in enumerate(word):
            subTrie.value += 1
            if char not in subTrie.children:
                subTrie.children[char] = Trie()
            subTrie = subTrie.children[char]
            if i == len(word) - 1:
                subTrie.value += 1

    for word in words:
        subtree = tree
        counts = 0
        for i, char in enumerate(word):
            if subtree.value == 1:
                answer += counts
                break
            elif i == len(word) - 1:
                answer += counts + 1
                break
            else:
                subtree = subtree.children[char]
                counts += 1

    return answer