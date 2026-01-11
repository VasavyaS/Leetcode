#
# Problem: 355. Design Twitter
# Difficulty: Medium
# Link: https://leetcode.com/problems/design-twitter/description/
# Language: python3
# Date: 2026-01-11


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list) #userId --> [count, tweetIds]
        self.followmap = defaultdict(set) #userId --> set of followerIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        if len(self.tweetmap) > 10:
            self.tweetmap.pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followmap[userId].add(userId)
        if len(self.followmap[userId]) >= 10:
            maxheap = []
            for followeeId in self.followmap[userId]:
                if followeeId in self.tweetsmap:
                    index = len(self.tweetmap[followeeIdId]) - 1
                    count, tweetId = self.tweetmap[followeeId][index]
                    heapq.heappush(maxheap, [-count, tweetId, followeeId, index - 1])

                    if len(maxheap) > 10:
                        heapq.heappop(maxheap)
                while maxheap:
                    count, tweetId, followeeId, index = heapq.heappop(maxheap)
                    heapq.heappush(minheap, [-count, tweetId, followeeId, index])
        else:
            for followeeId in self.followmap[userId]:
                if followeeId in self.tweetmap:
                    index = len(self.tweetmap[followeeId]) - 1
                    count, tweetId = self.tweetmap[followeeId][index]
                    heapq.heappush(minheap, [count, tweetId, followeeId, index - 1])
        
        while minheap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
