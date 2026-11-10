class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timeStamp, tweetId])
        self.timeStamp += 1
               
    def getNewsFeed(self, userId: int) -> List[int]:
        output = []
        maxHeap = []

        # Add user to follows since own tweets part of news feed
        self.follows[userId].add(userId)

        # Add most recent tweet from each followee to maxHeap
        for followeeId in self.follows[userId]:
            if followeeId in self.tweets:
                # Index of most recent tweet
                i = len(self.tweets[followeeId]) - 1
                timeStamp, tweetId = self.tweets[followeeId][i]
                maxHeap.append([timeStamp, tweetId, followeeId, i])

        heapq.heapify_max(maxHeap)

        while maxHeap and len(output) < 10:
            timeStamp, tweetId, followeeId, i = heapq.heappop_max(maxHeap)
            output.append(tweetId)
            # Add next most recent tweet to maxHeap
            if i > 0:
                timeStamp, tweetId = self.tweets[followeeId][i - 1]
                heapq.heappush_max(maxHeap, [timeStamp, tweetId, followeeId, i - 1])
            
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
