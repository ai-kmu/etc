<h3>11. Container With Most Water</h3>

https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

![image](https://user-images.githubusercontent.com/76420366/158053825-03414533-f5f2-4115-a7a4-7b454786dc08.png)

Input: height = [1,8,6,2,5,4,8,3,7]</br>
Output: 49</br>
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]</br>
Output: 1



Constraints:

- n == height.length</br>
- 2 <= n <= 105</br>
- 0 <= height[i] <= 104
