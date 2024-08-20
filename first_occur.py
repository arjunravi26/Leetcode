# Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        length = len(haystack) - needle_len + 1
        if haystack == needle:
            return 0
        for i in range(length):
            if needle == haystack[i:i+needle_len]:
                return i
        return -1
