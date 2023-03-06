class Solution:
    # O(n) time | O(n) space
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = {}
        for letter in s:
            if letter not in map:
                map[letter] = 1
            else:
                map[letter] += 1

        for letter in t:
            if letter in map and map[letter] > 0:
                map[letter] -= 1
                if map[letter] == 0:
                    del map[letter]
            else:
                return False
        return len(map) == 0
