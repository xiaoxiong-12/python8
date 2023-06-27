#!/usr/bin/python
# author Yu
# 2023年06月09日
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_length = 0
        my_set = set()
        for i in range(len(s)):
            while s[i] in my_set:
                my_set.remove(s[start])
                start += 1
            else:
                my_set.add(s[i])
                max_length = max(max_length, i - start + 1)
        return max_length


a = Solution()
b=a.lengthOfLongestSubstring("pwwkew")
print(b)

