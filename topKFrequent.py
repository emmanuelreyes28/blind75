class Solution:
    # O(n) time | O(n) space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # map to keep track of count for each num in nums list
        # create an array of empty arrays with the size being set to len of nums + 1 to account for the last num
        frequency = [[] for _ in range(len(nums) + 1)]

        # populate map with key and values pairs represnting the count for each value
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        # iterate through map and add each num to the index position that the num occurs
        for num, c in count.items():
            frequency[c].append(num)

        # this is going to get us k most frequent nums since the values are stored from
        # least to most frequent which is why we iterate through frequency array from left to right
        result = []
        for i in range(len(frequency) - 1, 0, -1):
            # iterate through each inner array and append its values to result
            for n in frequency[i]:
                result.append(n)
                # once we reach the length of k we are done
                if len(result) == k:
                    return result
