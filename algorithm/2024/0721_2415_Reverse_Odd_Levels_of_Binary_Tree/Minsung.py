class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def reverseOddLevels(self, root):
        '''
        Step1
            각 level 별 value들을 list 형태로 저장 
            O(n)
        Step 2
            odd-level list만 reverse
            O(n)
        Step 3
            저장된 level 별 list -> TreeNode
            O(n)
        '''
        self.level_value = [[] for _ in range(15)]  # 최대 node의 수는 2**14
        self.level = 0
        self.count = 0
        from collections import deque
        self.queue = deque([root])
        # Step 1
        while self.queue:
            self.Step_1()
        '''
        self.level_list 결과 예시
        [[2], [3, 5], [8, 13, 21, 34], [], [], [], [], [], [], [], [], [], [], [], []]
        '''

        # Step 2
        for i, cur_level_value in enumerate(self.level_value):
            if i%2 == 1:  # 홀 수 level 경우, reverse
                self.level_value[i] = cur_level_value[::-1]
        '''
        self.level_list 결과 예시
        [[2], [5, 3], [8, 13, 21, 34], [], [], [], [], [], [], [], [], [], [], [], []]
        '''

        # Step 3
        reversed_root = TreeNode()
        self.queue = deque([reversed_root])
        self.level = 0
        self.count = 0
        while self.queue:
            self.Step_3()
        return reversed_root
    
    def Step_3(self):
        cur_node = self.queue.popleft()
        cur_node.val = self.level_value[self.level][self.count]
        try:  # leaf node일 경우, index error 발생하므로 except 처리 
            cur_node.left = TreeNode(val=self.level_value[self.level+1][self.count*2], left=None, right=None)
            cur_node.right = TreeNode(val=self.level_value[self.level+1][self.count*2+1], left=None, right=None)
            self.queue.append(cur_node.left)
            self.queue.append(cur_node.right)
        except:
            pass
        self.count += 1
        if self.count == 2 ** self.level:
            self.level += 1
            self.count = 0
        
    def Step_1(self):
        '''
        self.level: 현재 node의 level
        self.count: 햔재 level 중 현재 node의 위치 
        '''
        cur_node = self.queue.popleft()
        self.level_value[self.level].append(cur_node.val)
        self.count += 1
        if self.count == 2 ** self.level:  # 현재 node가 현재 level의 마지막 node일 경우, level 추가
            self.level += 1
            self.count = 0
        if cur_node.left == None: 
            return
        self.queue.append(cur_node.left)
        self.queue.append(cur_node.right)
