# fail code

from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        layer = 0
        layer_len = 2**layer
        count = 0

        node_list = deque([root])

        while node_list:
            node = node_list.popleft()

            # 바꾸기
            if layer % 2 == 1 and count + 1 < layer_len:
                node.val, node_list[layer_len - 2*(count+1)].val = node_list[layer_len - 2*(count+1)].val, node.val
            count += 1
            if count == layer_len:
                layer += 1
                layer_len = 2**layer
                count = 0

            if node.left is not None:
                node_list.append(node.left)
                node_list.append(node.right)

        return root   
