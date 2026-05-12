#
# Problem: 359. Logger Rate Limiter
# Difficulty: Easy
# Link: https://leetcode.com/problems/logger-rate-limiter/description/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-three-months
# Language: python3
# Date: 2026-05-12


class Logger:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.hashmap:
            time = self.hashmap[message]
            if timestamp < time + 10:
                return False
            else:
                self.hashmap[message] = timestamp
                return True
        else:
            self.hashmap[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
