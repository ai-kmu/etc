#!/usr/bin/env python
# coding: utf-8

# In[16]:


def solution(str1, str2):
    answer = 0
    str1_list=[]
    #두글자씩 끊어서 입력 받기
    #print(len(str1))
    str2_list=[]
    def search_word_str1(i=0):
        if  len(str1)-1 > i:
            input_word_str1 = str1[i]+str1[i+1]
            input_word_str1 = input_word_str1.lower()
            if ord(str1[i].lower()) > 96 and ord(str1[i].lower()) < 123:
                if ord(str1[i+1].lower()) > 96 and ord(str1[i].lower()) < 123:
                    str1_list.append(input_word_str1)    
            now_str1=i+1
            search_word_str1(now_str1)
    
    def search_word_str2(i=0):
        if  len(str2)-1 > i:
            input_word_str2 = str2[i]+str2[i+1]
            input_word_str2 = input_word_str2.lower()
            if ord(str2[i].lower()) > 96 and ord(str2[i].lower()) < 123:
                if ord(str2[i+1].lower()) > 96 and ord(str2[i].lower()) < 123:
                    str2_list.append(input_word_str2)    
            now_str2=i+1
            search_word_str2(now_str2)

    
    
    
    search_word_str1()
    search_word_str2()
    
    all_list=[]
    
    for i in range(len(str1_list)):
        all_list.append(str1_list[i])
    for j in range(len(str2_list)):
        all_list.append(str2_list[j])
    all_list = list(set(all_list))
    
    inter_list=[]
    

                
    str1_set = set(str1_list)
    str2_set = set(str2_list)
    inter_list = list(str1_set & str2_set)
    print(str1_list)
    print(str2_list)
    #print(all_list)
    #print(inter_list)
    
    if len(all_list) == 0 :
        answer = 65536
    else:
        answer = len(inter_list) / len(all_list)
        answer = answer * 65536
        
    
    return answer


# In[ ]:




