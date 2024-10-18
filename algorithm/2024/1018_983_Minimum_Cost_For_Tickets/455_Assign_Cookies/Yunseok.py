class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # content_count = 0
        # is_used_cookie = [False] * len(s)
        # for idx_i, child_elem in enumerate(g):
        #     for idx_j, cookie_elem in enumerate(s):

        content_count = 0
        # removing_idx_list_child = []
        # removing_idx_list_cookie = []
        # for idx_i, child_elem in enumerate(g):
        #     if child_elem in s:
        #         s.remove(child_elem)
        #         removing_idx_list_child.append(child_elem)
        #         content_count += 1

        # for idx_elem in removing_idx_list_child:
        #     g.remove(idx_elem)

        # g.sort()
        # s.sort()
        # print(g)
        # print(s)

        # for cookie_elem in s:
        #     if child_elem in g:
        #         if cookie_elem >= child_elem:
        #             content_count += 1
        #         break



        # # for cookie_elem in s:
        # #     for child_left_elem in g:
        # #         if cookie_elem > child_left_elem:
        # #             content_count += 1
        # #             break

        g.sort(reverse=True)
        s.sort()

        # for child_elem in g:
        #     for cookie_elem in s:
        #         if cookie_elem >= child_elem:
        #             content_count += 1
        #             s.remove(cookie_elem)
                
        #         break

        if len(s) == 0:
            return 0

        if g[len(g) - 1] > s[len(s) - 1]:
            return 0

        used_elem = [False] * len(s)
        for cookie_elem_idx, cookie_elem in enumerate(s):
            for child_elem in g:
                if cookie_elem >= child_elem and used_elem[cookie_elem_idx] is False:
                    content_count += 1
                    g.remove(child_elem)
                    used_elem[cookie_elem_idx] = True


        return content_count
            
