class Solution:
    # O(n) space | O(n) time
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        create a left and right pointer to keep track of longest substring
        as long as the next letter in the string does not already exist in the current
        substring then go ahead and add it and increment the right pointer by 1. Otherwise,
        increment left pointer by 1.

        continuosly check the max len of the current longest substring and the potential
        longest substring and update accordingly.

        use a set for a O(1) look up
        '''

        charSet = set()
        left = 0
        longestSubstring = 0

        for right in range(len(s)):
            while s[right] in charSet:
                # remove the repeated char from set and update window by incrementing left
                charSet.remove(s[left])
                left += 1
            # keep the repeated char now that left pointer has been updated
            charSet.add(s[right])
            # add one since we are using indexes to take diff
            longestSubstring = max(longestSubstring, right - left + 1)
        return longestSubstring
