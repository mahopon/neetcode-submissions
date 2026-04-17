class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = defaultdict(int)
        left, right = 0, 0
        max_substring = 1
        while right < len(s):
            if s[right] in res and res[s[right]] >= left:
                left = res[s[right]] + 1
            res[s[right]] = right
            max_substring = max(max_substring, right - left + 1)
            right += 1
        return max_substring