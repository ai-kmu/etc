import sys
r=sys.stdin.readline
Line_num=int(r())

dic={}

while Line_num:
	p1,p2=map(int,r().split())
	dic[p1]=p2
	Line_num-=1

p1_list=sorted(dic.keys())
one_line=[p1_list[0],dic[p1_list[0]]]

total_dist=0

for i in p1_list[1:]:
	if one_line[1]<i:
		total_dist+=one_line[1]-one_line[0]
		one_line=[i,dic[i]]
	else:
		if one_line[1]<dic[i]:
		    one_line[1]=dic[i]
total_dist+=one_line[1]-one_line[0]

print(total_dist)