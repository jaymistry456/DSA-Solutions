# https://leetcode.com/problems/design-twitter/

class Twitter:

    def __init__(self):
        self.tweetNo = 0
        self.followees = defaultdict(set)    # person -> set of followees
        self.tweetMap = defaultdict(list)    # person -> list of (tweetNo, tweetId)

    # TC: O(1), SC: O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetNo += 1
        self.tweetMap[userId].append((self.tweetNo, tweetId))

    # TC: O(nlogn), SC: O(n) where n = no. of tweets of all the followees of user
    def getNewsFeed(self, userId: int) -> List[int]:
        self.followees[userId].add(userId)
        maxHeap = []    # (-tweetNo, tweetId)
        for followeeId in self.followees[userId]:
            for tweetNo, tweetId in self.tweetMap[followeeId]:
                heapq.heappush(maxHeap, (-tweetNo, tweetId))
        res = []
        for _ in range(min(len(maxHeap), 10)):
            res.append(heapq.heappop(maxHeap)[1])
        return res

    # TC: O(1), SC: O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    # TC: O(1), SC: O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)