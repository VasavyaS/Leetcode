#
# Problem: 380. Insert Delete GetRandom O(1)
# Difficulty: Medium
# Link: https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-all
# Language: python3
# Date: 2026-05-26


class RandomizedSet:

    def __init__(self):
        self.listNums = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.hashmap)
            self.listNums.append(val)
            return True
        return False      

    def remove(self, val: int) -> bool:
        #move the val to the end of the list. Update the index in hashmap and delete the val
        if val in self.hashmap:
            idx = self.hashmap[val]
            self.hashmap[self.listNums[-1]] = idx
            self.listNums[idx] = self.listNums[-1]
            self.listNums.pop()
            del self.hashmap[val]
            return True
        return False       

    def getRandom(self) -> int:
        return random.choice(self.listNums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
