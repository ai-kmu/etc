#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
        }

        if digits =="":
            return []
        
        digits_list = []
        for i in range(len(digits)):
            digits_list.append(digits[i])
            
        output=[]
        def addword(letter='',i=0):
            if len(digits_list)>i:
                digit = digits_list[i]
                for add_digit in dic[digit]:
                    now = letter + add_digit
                    addword(now,i+1)
            else:
                output.append(letter)
        
        addword()
        return output

