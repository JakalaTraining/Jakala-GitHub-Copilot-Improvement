# Debugging Exercise: LRU Cache

## Objective
Identify and fix a bug in the LRU Cache code.

## Track
You are given an implementation of the `LRUCache` class that should meet the specifications of a Least Recently Used (LRU) cache. However, it has some bugs that prevent it from working properly.

## Steps:
1. Analyze the code provided below by entering comments and try to figure out where the error is.
2. Fix the bugs and explain the change made.
3. Verify that the cache is behaving correctly by running the tests provided:

## Codice:
```java
public class Main {
    public static void main(String[] args) {
        LRUCache lruCache = new LRUCache(2);
        lruCache.put(1, 10);
        lruCache.put(2, 20);
        System.out.println(lruCache.get(1)); // Output atteso: 10
        lruCache.put(3, 30); // Rimuove il meno usato (2)
        System.out.println(lruCache.get(2)); // Output atteso: -1
    }
}
```
```python
def main():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 10)
    lru_cache.put(2, 20)
    print(lru_cache.get(1))  # Output atteso: 10
    lru_cache.put(3, 30)     # Rimuove il meno usato (2)
    print(lru_cache.get(2))  # Output atteso: -1

if __name__ == "__main__":
    main()
```

# Test Generation Exercise: LRU Cache

## Objective
Generate tests to verify the proper operation of the LRU Cache class.

## Track
You are given an implementation of the `LRUCache` class that should meet the specification of a Least Recently Used (LRU) cache. Your task is to generate tests to verify that the cache behaves correctly in various scenarios.

## Steps:
1. Analyze the code provided below and identify the test cases needed to verify that the cache is working properly.
2. Write tests for each identified case.
3. Run the tests and verify that the results are correct.

## Examples:
Generate unit tests for the LRUCache class using. Tests should verify:
1. The insertion and retrieval of values.
2. The removal of the least used node when the cache is full.
3. The updating of the value of an existing key.
4. The updating of node order when a key is accessed.
5. The behavior of the cache when the capacity is 1.

## Questions:
1. Do the tests cover all possible LRU Cache usage scenarios? If not, what other tests would you add?
2. If you were to improve your implementation, what would you change to make the code more robust?
3. If the cache were used in a high-load system, what optimizations could you implement?
