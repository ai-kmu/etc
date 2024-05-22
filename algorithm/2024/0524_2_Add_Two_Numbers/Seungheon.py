class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 마지막 노드부터 채우기 위해 reculsive 하게 구현
        def reculsive_sum(node1=l1, node2=l2, carry = 0):  
            ln = ListNode()
            node_sum = node1.val + node2.val + carry
            carry  = node_sum // 10 
            ln.val =  node_sum % 10 

            # 다음 node나 carry가 있을시 계속 수행  
            if node1.next or node2.next or carry:
                ln.next = reculsive_sum(node1.next if node1.next else ListNode(0), node2.next if node2.next else ListNode(0), carry)
            return ln

        return reculsive_sum()
