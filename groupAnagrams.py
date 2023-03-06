class Solution:
    # O(m * n) where m is the number of words given in list of strings and
    # where n is the number of lower case letters available (26)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)  # default value for a given key is a list

        for word in strs:
            # create array with fixed num of zeros (26) for each word in list of strings
            count = [0] * 26  # a -> z

            for letter in word:
                # count how many character we have for each word
                count[ord(letter) - ord("a")] += 1  # this is a list
            # group all words with the same count together in dict as a value using count as the key
            # if the count does not exist yet we will use a defaultdict to cover this edge case
            # key of dict cannot be a list so we turn it into tuple
            result[tuple(count)].append(word)
        # only return values from result dict
        return result.values()
