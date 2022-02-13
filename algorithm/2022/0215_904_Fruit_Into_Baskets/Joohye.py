#Sliding window 알고리즘 사용

class Solution(object):
    def totalFruit(self, tree):

        basket = set()
        last_tree_index = 0
        fast = slow = 0
        max_count = 0
        
        while fast < len(tree):
            basket.add(tree[fast])  #fruit을 basket에 담는다.
            
            
            if len(basket) <= 2: #basket 안에 두종류 이하의 과일이 들어있다면,
                
                #방문한 tree의 인덱스 저장
                if tree[last_tree_index] != tree[fast]:
                    last_tree_index = fast
                fast += 1
                max_count = max(max_count, fast - slow)
                           
            else:  #아니라면, 바구니안에 마지막으로 방문한 나무와,나무의 열매가 있어야 한다.
                basket = set([tree[last_tree_index], tree[fast]])
                slow = last_tree_index
        return max_count
