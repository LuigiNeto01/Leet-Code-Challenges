from typing import List, Dict, Set, Tuple
import heapq

class Twitter:
    def __init__(self):
        # timestamp counter to order tweets globally (monotonic increasing)
        self._time = 0
        # mapping userId -> list of (timestamp, tweetId); append newest at end
        self._tweets: Dict[int, List[Tuple[int, int]]] = {}
        # mapping followerId -> set of followeeIds
        self._follows: Dict[int, Set[int]] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # create list for user if missing
        if userId not in self._tweets:
            self._tweets[userId] = []
        # increment global time to ensure strict ordering
        self._time += 1
        # append (time, tweetId); newest tweets are at the end of the list
        self._tweets[userId].append((self._time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # gather all users whose tweets should appear: the user themself plus followees
        users = set()
        users.add(userId)
        # include followees if any
        if userId in self._follows:
            users.update(self._follows[userId])
        # max-heap simulation via min-heap of negative timestamps
        heap = []
        # For each user, if they have tweets, push their latest tweet along with indices
        for u in users:
            user_tweets = self._tweets.get(u)
            if user_tweets:
                idx = len(user_tweets) - 1  # index of newest tweet
                time, tid = user_tweets[idx]
                # push tuple: (-time, tweetId, userId, index)
                heapq.heappush(heap, (-time, tid, u, idx))
        result = []
        # extract up to 10 most recent tweets by repeatedly popping heap and pushing previous tweet from same user
        while heap and len(result) < 10:
            negtime, tid, u, idx = heapq.heappop(heap)
            result.append(tid)
            # move to previous tweet for this user if exists
            if idx - 1 >= 0:
                prev_time, prev_tid = self._tweets[u][idx - 1]
                heapq.heappush(heap, (-prev_time, prev_tid, u, idx - 1))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # cannot follow self; ignore such requests
        if followerId == followeeId:
            return
        # ensure follower's follow set exists
        if followerId not in self._follows:
            self._follows[followerId] = set()
        # add followee; duplicate adds are harmless due to set
        self._follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # cannot unfollow self; ignore
        if followerId == followeeId:
            return
        # if follower has followees, remove followee if present (no KeyError)
        if followerId in self._follows:
            self._follows[followerId].discard(followeeId)