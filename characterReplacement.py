class Solution:
    # O(n) time | O(1) space
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        for right in range(len(s)):
            # increment value of letter if it doesnt exist then make value = 0
            count[s[right]] = 1 + count.get(s[right], 0)
            # check if we have exceeded k opereations, if so increment left by 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1  # decrement value of letter at left index
                left += 1

            res = max(res, right - left + 1)

        return res
