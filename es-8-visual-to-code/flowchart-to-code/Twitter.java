import java.util.*;

public class Twitter {
    private static int timestamp = 0;

    // Tweet class to store tweet id and time
    private static class Tweet {
        int id;
        int time;
        public Tweet(int id, int time) {
            this.id = id;
            this.time = time;
        }
    }

    // userId -> list of tweets (most recent first)
    private Map<Integer, List<Tweet>> userTweets;
    // userId -> set of followees
    private Map<Integer, Set<Integer>> followers;

    public Twitter() {
        userTweets = new HashMap<>();
        followers = new HashMap<>();
    }

    // Publish a tweet
    public void postTweet(int userId, int tweetId) {
        userTweets.putIfAbsent(userId, new LinkedList<>());
        userTweets.get(userId).add(0, new Tweet(tweetId, timestamp++));
    }

    // View recent tweets (news feed)
    // Returns up to 10 most recent tweet ids in the user's news feed.
    // Each item in the news feed must be posted by users who the user followed or by the user themself.
    public List<Integer> getNewsFeed(int userId) {
        PriorityQueue<Tweet> pq = new PriorityQueue<>((a, b) -> b.time - a.time);

        // Add user's tweets
        if (userTweets.containsKey(userId)) {
            pq.addAll(userTweets.get(userId));
        }

        // Add followees' tweets
        Set<Integer> followees = followers.getOrDefault(userId, new HashSet<>());
        for (int followeeId : followees) {
            if (userTweets.containsKey(followeeId)) {
                pq.addAll(userTweets.get(followeeId));
            }
        }

        // Get top 10 tweets
        List<Integer> res = new ArrayList<>();
        int count = 0;
        while (!pq.isEmpty() && count < 10) {
            res.add(pq.poll().id);
            count++;
        }
        return res;
    }

    // Follow a user
    public void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return; // Can't follow yourself
        followers.putIfAbsent(followerId, new HashSet<>());
        followers.get(followerId).add(followeeId);
    }

    // Unfollow a user
    public void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) return; // Can't unfollow yourself
        Set<Integer> followees = followers.get(followerId);
        if (followees != null) {
            followees.remove(followeeId);
        }
    }

    // Simple main to demo the flow
    public static void main(String[] args) {
        Twitter twitter = new Twitter();

        // Publish a tweet
        twitter.postTweet(1, 101); // User 1 tweets 101

        // User 2 follows user 1
        twitter.follow(2, 1);

        // User 2's news feed should have tweet 101
        System.out.println("User 2's feed: " + twitter.getNewsFeed(2)); // [101]

        // User 2 unfollows user 1
        twitter.unfollow(2, 1);

        // User 2's feed (should be empty)
        System.out.println("User 2's feed after unfollow: " + twitter.getNewsFeed(2)); // []
    }
}