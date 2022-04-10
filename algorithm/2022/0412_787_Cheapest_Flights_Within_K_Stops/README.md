# 787. Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/


There are n cities connected by some number of flights.<br>
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.<br>
If there is no such route, return -1.

example 1.

![image](https://user-images.githubusercontent.com/76420366/162621349-f03536bc-0394-4bf3-943a-a247d8348de2.png)

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1<br>
Output: 700<br>
Explanation:<br>
The graph is shown above.<br>
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.<br>
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.<br>

example 2.

![image](https://user-images.githubusercontent.com/76420366/162621384-5a2422c2-bd90-47f8-a1a2-1c01bdb9257a.png)

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1<br>
Output: 200<br>
Explanation:<br>
The graph is shown above.<br>
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.<br>

example 3.

![image](https://user-images.githubusercontent.com/76420366/162621406-5e950c76-5b38-43c2-875e-db6d1112b5ce.png)


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0<br>
Output: 500<br>
Explanation:<br>
The graph is shown above.<br>
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.<br>
