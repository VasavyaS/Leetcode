#
# Problem: 933. Number of Recent Calls
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-recent-calls/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-06


class RecentCounter:

    def __init__(self):
        self.calls = deque()

    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls[0] < t - 3000:
            self.calls.popleft()
        return len(self.calls)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
