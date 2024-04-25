class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for element in nums:
            if element not in hashmap:
                hashmap[element] = 1
            else:
                return element
        