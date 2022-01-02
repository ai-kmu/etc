# 97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1

The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

![image](https://user-images.githubusercontent.com/76420366/147863819-47c9565f-d6e8-47d6-8dad-3b6e7abcdf07.png)

example 1)</br>
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"</br>
Output: true

example 2)</br>
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"</br>
Output: false

example 3)</br>
Input: s1 = "", s2 = "", s3 = ""</br>
Output: true

Constraints:</br>
0 <= s1.length, s2.length <= 100</br>
0 <= s3.length <= 200</br>
s1, s2, and s3 consist of lowercase English letters.
