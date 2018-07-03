---
title: '[ACM][BestCoder]两次的DP'
tags:
  - 算法
id: 379
categories:
  - 算法
date: 2015-07-14 23:06:19
---



# Senior's String

 Accepts: 30
 Submissions: 286

 Time Limit: 2000/1000 MS (Java/Others)
 Memory Limit: 65536/65536 K (Java/Others)




Problem Description


Xuejiejie loves strings most. In order to win the favor of her, a young man has two strings X, Y to Xuejiejie. Xuejiejie has never seen such beautiful strings! These days, she is very happy. But Xuejiejie is missish so much, in order to cover up her happiness, she asks the young man a question. In face of Xuejiejie, the young man is flustered. So he asks you for help.

The question is that : Define the L as the length of the longest common subsequence of X and Y.( The subsequence does not need to be continuous in the string, and a string of length L has 2L subsequences containing the empty string ). Now Xuejiejie comes up with all subsequences of length L of string X, she wants to know the number of subsequences which is also the subsequence of string Y.




Input


In the first line there is an integer T, indicates the number of test cases.

In each case:

The first line contains string X, a non-empty string consists of lowercase English letters.

The second line contains string Y, a non-empty string consists of lowercase English letters.

1≤|X|,|Y|≤1000, |X| means the length of X.




Output


For each test case, output one integer which means the number of subsequences of length L of X which also is the subsequence of string Y modulo 109+7.




Sample Input


```
2
a
b
aa
ab
```




Sample Output


```
1
2
```




大意就是说求具有相同长度的LCS的子串的个数....
首先处理出LCS是一个nm的算法，dp可以YY出来，然后再用一次DP，
用f[i][j]表示在X串的前i个字符中，有多少个长度为dp[i][j]的子序列在Y的前j个字符中也出现了。转移：若dp[i−1][j]==dp[i][j]，则f[i][j]+=f[i−1][j]，表示i这个字符不选；再考虑选i这个字符，找到Y串前j个字符中最靠后的与X[i]匹配的字符的位置，设为p，若dp[i−1][p−1]+1==dp[i][j]，则f[i][j]+=f[i−1][p−1]。最终的答案即为f[n][m]。