
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.visit_list = [homepage]
        self.cur_point = 0
        
        
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.visit_list = self.visit_list[:self.cur_point+1]
        self.visit_list.append(url)
        self.cur_point += 1
        return 

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.cur_point - steps < 0:
            self.cur_point = 0
        else:
            self.cur_point -= steps
        return self.visit_list[self.cur_point]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.cur_point + steps > len(self.visit_list)-1:
            self.cur_point = len(self.visit_list)-1
        else:
            self.cur_point += steps
        return self.visit_list[self.cur_point]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
