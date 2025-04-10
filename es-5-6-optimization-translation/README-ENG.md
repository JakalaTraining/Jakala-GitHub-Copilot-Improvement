# 🔁 EXERCISE 5: Adaptability Between Programming Languages

## 🆚 Comparison Between the **C#** and **JavaScript** Versions

### ✅ Objective
Translate and analyze a `Twitter` class from C# to JavaScript, evaluating:
- Syntactic and semantic differences  
- Alternative data structures  
- Performance implications  
- Adaptation strategy  

---

## 1. 📦 Data Structures Used

| C#                           | JavaScript                    |
|-----------------------------|-------------------------------|
| `Dictionary<int, List<>>`   | `Map<number, Array<>>`        |
| `HashSet<int>`              | `Set<number>`                 |
| `List<(int, int)>`          | `Array<[number, number]>`     |
| `PriorityQueue`             | `Manual Heap / Array + sort`  |

JavaScript does not have a native `PriorityQueue`, but it can be simulated:
- With external libraries (`heap.js`)  
- With a sorted array (simpler approach for exercises)

---

## 2. 🔄 Conceptual Translation of the Logic

### 📥 `postTweet(userId, tweetId)`
- C#: adds to list, sorts by descending timestamp  
- JS: `this.count--` creates negative timestamps → newer = smaller

### 📰 `getNewsFeed(userId)`
- C#: Uses `PriorityQueue` to combine own and followees' tweets  
- JS: Requires alternative implementation (manual heap or sorted array)

### ➕➖ `follow()` / `unfollow()`
- C#: uses `Dictionary<int, HashSet<int>>`  
- JS: `Map<number, Set<number>>` used to simulate it

---

## 3. ⏱️ Time Complexity Analysis

**Goal of `getNewsFeed`:**  
Return the 10 most recent tweets of the user and their followees.

### ✅ Expected Complexity:
- Iterate over followees (n): `O(n)`  
- Insert up to 10 tweets per user into a heap: `O(n log k)` with `k = n × 10`  
- Extract 10 tweets: `O(10 log k)` → constant

➡️ **Result:** `O(n log n)` with `c=10` as a constant

---

## 4. 🔧 JavaScript Implementation of the Twitter Class

```javascript
class Twitter {
  constructor() {
    this.tweetMap = new Map();        // userId → Array<[timestamp, tweetId]>
    this.followMap = new Map();       // userId → Set<userId>
    this.count = 0;                   // Simulates timestamp
  }

  postTweet(userId, tweetId) {
    if (!this.tweetMap.has(userId)) {
      this.tweetMap.set(userId, []);
    }
    this.tweetMap.get(userId).push([this.count--, tweetId]);
    if (this.tweetMap.get(userId).length > 10) {
      this.tweetMap.get(userId).shift();  // Removes oldest tweet
    }
  }

  follow(followerId, followeeId) {
    if (!this.followMap.has(followerId)) {
      this.followMap.set(followerId, new Set());
    }
    this.followMap.get(followerId).add(followeeId);
  }

  unfollow(followerId, followeeId) {
    if (this.followMap.has(followerId)) {
      this.followMap.get(followerId).delete(followeeId);
    }
  }

  getNewsFeed(userId) {
    const tweets = [];

    // Include user's own tweets
    if (this.tweetMap.has(userId)) {
      tweets.push(...this.tweetMap.get(userId));
    }

    // Include tweets from followees
    const followees = this.followMap.get(userId) || new Set();
    for (const followeeId of followees) {
      if (this.tweetMap.has(followeeId)) {
        tweets.push(...this.tweetMap.get(followeeId));
      }
    }

    // Sort by descending timestamp (most recent first)
    tweets.sort((a, b) => a[0] - b[0]);

    // Return only the latest 10 tweetIds
    return tweets.slice(0, 10).map(([_, tweetId]) => tweetId);
  }
}
```

---

## 5. 🧠 Final Observations and Best Practices

### 📌 Heap Simulation  
To faithfully replicate the C# version, consider replacing `.sort()` with an explicit binary heap.

### 📌 Edge Case Handling  
- User with no tweets → `tweetMap.get()` returns `undefined`  
- User following no one → `followMap.get()` returns empty `Set`

---

## 6. ✍️ Prompt Suggestions and Future Extensions

When asking Copilot similar tasks:  
> ✨ "Implement the `getNewsFeed()` function in JavaScript so that it returns the 10 most recent tweets of a user and their followees, using a heap (or simulation) to maintain time order."

Other effective prompts:
- "Limit tweets to 10 per user and sort by descending timestamp."
- "Manage follow/unfollow using `Map` and `Set`."
- "Implement a `PriorityQueue` to simulate the native C# structure."

---

# EXERCISE 6: Analysis of GitHub Copilot Chat Outputs

## Correctness of the Complexity Analysis

Without access to the full implementation of `getNewsFeed()` in the original C# class, it's difficult to verify the analysis completely. However, Copilot’s "O(n log k)" worst-case estimate seems plausible, considering:

1. The need to iterate over all followed users (component "n")  
2. The use of a heap (PriorityQueue) to maintain and retrieve the most recent tweets (component "log k")

## Meaning of n and k

Copilot defines:
- n = number of followed users  
- k = maximum number of tweets (up to 10 per user)

This definition is partially correct but slightly inaccurate:
- **n** is correctly identified as the number of followed users  
- **k** is better interpreted as the total number of tweets considered (which can be up to n×10, where 10 is the tweet-per-user limit)

## Impact of the 10-Tweet Limit on Complexity

The 10-tweet-per-user limit significantly impacts complexity:

1. **Smaller Heap Size**: The heap will hold at most n×10 tweets (not the whole platform's tweets)  
2. **Constant Time per User**: Since the number of tweets per user is limited, operations per user are O(1) instead of depending on that user's tweet count  
3. **Effective Complexity**: Since 10 is a constant, the complexity simplifies to O(n log n) instead of O(n log k), because k ≤ 10n, so log k is roughly log n plus a constant

## Improved Version of the Explanation

A more precise explanation of the time complexity of `getNewsFeed()` would be:

"The time complexity of getNewsFeed() is O(n log(n×c)), where:
- n is the number of followed users
- c is the constant tweet limit per user (10 in this case)

The process can be broken down as:
1. Iterate over each of the n followed users: O(n)  
2. For each user, extract their recent tweets (max 10): O(1) per user  
3. Insert these tweets into a heap of size up to n×10: each insertion costs O(log(n×10))  
4. Extract the 10 most recent tweets from the heap: O(10 log(n×10))

Since c = 10 is constant, this simplifies to O(n log n).

The most expensive step is managing the heap during the merge of tweets from different users, which involves logarithmic sorting operations relative to the heap size."

--- 