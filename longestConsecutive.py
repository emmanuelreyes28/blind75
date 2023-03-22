class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequency by verifying if the num before it is in the set
            if(n - 1) not in numSet:  # if not in the set check thr num after and track the lenght of the sequence
                length = 0
                while (n + length) in numSet:
                    length += 1
                # take the greater sequence btwn length and longest
                longest = max(length, longest)
        return longest
