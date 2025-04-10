using System;
using System.Collections.Generic;

public class Twitter
{
    private int count;
    private Dictionary<int, List<int[]>> tweetMap;
    private Dictionary<int, HashSet<int>> followMap;

    public Twitter()
    {
        this.count = 0;
        this.tweetMap = new Dictionary<int, List<int[]>>();
        this.followMap = new Dictionary<int, HashSet<int>>();
    }

    public void PostTweet(int userId, int tweetId)
    {
        if (!tweetMap.ContainsKey(userId))
        {
            tweetMap[userId] = new List<int[]>();
        }
        tweetMap[userId].Add(new int[] { count, tweetId });
        if (tweetMap[userId].Count > 10)
        {
            tweetMap[userId].RemoveAt(0);
        }
        count--;
    }

    public List<int> GetNewsFeed(int userId)
    {
        var res = new List<int>();
        var minHeap = new PriorityQueue<int[], int>(Comparer<int>.Default);

        if (!followMap.ContainsKey(userId))
        {
            followMap[userId] = new HashSet<int>();
        }
        followMap[userId].Add(userId);

        foreach (var followeeId in followMap[userId])
        {
            if (!tweetMap.ContainsKey(followeeId)) continue;

            var tweets = tweetMap[followeeId];
            int index = tweets.Count - 1;
            var tweet = tweets[index];
            minHeap.Enqueue(new int[] { tweet[0], tweet[1], followeeId, index - 1 }, tweet[0]);
        }

        while (minHeap.Count > 0 && res.Count < 10)
        {
            var top = minHeap.Dequeue();
            res.Add(top[1]);
            int nextIndex = top[3];
            if (nextIndex >= 0)
            {
                var tweets = tweetMap[top[2]];
                var nextTweet = tweets[nextIndex];
                minHeap.Enqueue(new int[] { nextTweet[0], nextTweet[1], top[2], nextIndex - 1 }, nextTweet[0]);
            }
        }

        return res;
    }

    public void Follow(int followerId, int followeeId)
    {
        if (!followMap.ContainsKey(followerId))
        {
            followMap[followerId] = new HashSet<int>();
        }
        followMap[followerId].Add(followeeId);
    }

    public void Unfollow(int followerId, int followeeId)
    {
        if (followMap.ContainsKey(followerId))
        {
            followMap[followerId].Remove(followeeId);
        }
    }
}