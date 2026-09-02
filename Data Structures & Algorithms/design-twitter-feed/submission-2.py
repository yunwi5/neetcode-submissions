class Twitter:

    def __init__(self):
        # key: user id, value: set of user Ids that user follows (followers)
        self.followersByUserId = {} 
        # key: user id, value: tweet ids list (oldest first item)
        self.tweetsByUserId = {}
        self.counter = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        # Time: O(n)
        # Space: O(1)
        if userId not in self.tweetsByUserId:
            self.tweetsByUserId[userId] = []
        self.tweetsByUserId[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Time: O(nlog(n))
        # Space: O(N*M + N*m + n)
        #
        # n = number of followeeIds of user

        relevantTweets = []
        if userId in self.tweetsByUserId:
            relevantTweets += self.tweetsByUserId[userId]
        
        if userId in self.followersByUserId:
            for followerId in self.followersByUserId[userId]:
                if followerId in self.tweetsByUserId:
                    relevantTweets += self.tweetsByUserId[followerId]
            
        minHeap = []
        for tweet in relevantTweets:
            heapq.heappush(minHeap, tweet)

            if len(minHeap) > 10:
                heapq.heappop(minHeap)
        
        result = []
        while minHeap:
            time, tweetId = heapq.heappop(minHeap)
            result.append(tweetId)

        result.reverse()
        return result
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followersByUserId:
            self.followersByUserId[followerId] = set()
        self.followersByUserId[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followersByUserId:
            return
        
        self.followersByUserId[followerId].discard(followeeId)

