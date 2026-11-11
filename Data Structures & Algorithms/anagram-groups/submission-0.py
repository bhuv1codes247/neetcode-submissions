class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = {}

        for word in strs:

            # Sort the characters
            key = ''.join(sorted(word))

            # If key doesn't exist, create an empty list
            if key not in freq:
                freq[key] = []

            # Add the original word to that list
            freq[key].append(word)

        return list(freq.values())
        