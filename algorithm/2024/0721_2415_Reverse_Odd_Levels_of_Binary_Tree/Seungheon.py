
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # 각 even layer의 절반을 순서 교환

        node_list = [root]
        even = False
        while node_list[0] is not None:
            layer_len = len(node_list)
            next_node_list = []

            # layer 마다 순서 교환
            for i in range(layer_len):
                # 새로운 node list 만들기
                next_node_list.append(node_list[i].left)
                next_node_list.append(node_list[i].right)
                if even and i < layer_len/2 :
                    node_list[i].val, node_list[-i-1].val = node_list[-i-1].val, node_list[i].val
            node_list = next_node_list
            # Flag 변경
            even = ~even

        return root   
