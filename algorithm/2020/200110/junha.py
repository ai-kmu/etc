import sys
r=sys.stdin.readline
Line_num=int(r())

# 한줄에 있는 2개의 점을 dictionary에 저장
dic={}

while Line_num:
	p1,p2=map(int,r().split())
	dic[p1]=p2
	Line_num-=1

# 첫번째 점들만 저장 
p1_list=sorted(dic.keys())
one_line=[p1_list[0],dic[p1_list[0]]]

total_dist=0

for i in p1_list[1:]:
	if one_line[1]<i:	# Is the Blank.
		total_dist+=one_line[1]-one_line[0]
		one_line=[i,dic[i]]	# make new start point
	else:
		if one_line[1]<dic[i]:	# Change one_line's p2
		    one_line[1]=dic[i]
total_dist+=one_line[1]-one_line[0]	# Meet Last line

print(total_dist)
