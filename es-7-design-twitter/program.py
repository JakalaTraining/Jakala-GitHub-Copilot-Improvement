import heapq

class Tweet:
    """
    Classe che rappresenta un tweet con un ID utente, un ID tweet e un timestamp.
    """
    def __init__(self, userId, tweetId, timestamp):
        self.userId = userId
        self.tweetId = tweetId
        self.timestamp = timestamp

class User:
    """
    Classe che rappresenta un utente con un ID e un insieme di utenti seguiti.
    """
    def __init__(self, userId):
        self.userId = userId
        self.following = set()

    def follow(self, followeeId):
        # Aggiunge un utente alla lista dei seguiti
        self.following.add(followeeId)

    def unfollow(self, followeeId):
        # Rimuove un utente dalla lista dei seguiti
        self.following.discard(followeeId)

class Twitter:
    """
    Classe principale che gestisce i tweet, gli utenti e le relazioni tra di loro.
    """
    def __init__(self):
        self.tweets = []  # Lista di oggetti Tweet
        self.users = {}  # Dizionario {userId: User}
        self.timestamp = 0  # Timestamp crescente per ordinare i tweet

    def post_tweet(self, userId, tweetId):
        # Crea un nuovo utente se non esiste
        if userId not in self.users:
            self.users[userId] = User(userId)
        # Aggiunge un nuovo tweet
        tweet = Tweet(userId, tweetId, self.timestamp)
        self.tweets.append(tweet)
        self.timestamp += 1

    def follow(self, followerId, followeeId):
        # Crea nuovi utenti se non esistono
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        # Aggiunge la relazione di follow
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId, followeeId):
        # Rimuove la relazione di follow se l'utente esiste
        if followerId in self.users:
            self.users[followerId].unfollow(followeeId)

    def get_feed(self, userId):
        # Recupera i 10 tweet più recenti dall'utente e dagli utenti seguiti
        if userId not in self.users:
            return []
        feed = []
        followed_users = self.users[userId].following | {userId}
        
        # Usa un heap per mantenere i 10 tweet più recenti
        for tweet in self.tweets:
            if tweet.userId in followed_users:
                heapq.heappush(feed, (tweet.timestamp, tweet.tweetId))
                if len(feed) > 10:
                    heapq.heappop(feed)
        
        # Ordina i tweet per timestamp decrescente
        return [tweetId for _, tweetId in sorted(feed, reverse=True)]

if __name__ == "__main__":
    twitter = Twitter()

    # Posta alcuni tweet
    twitter.post_tweet(1, 101)  # Utente 1 posta il tweet 101
    twitter.post_tweet(2, 102)  # Utente 2 posta il tweet 102
    twitter.post_tweet(1, 103)  # Utente 1 posta il tweet 103
    twitter.post_tweet(3, 104)  # Utente 3 posta il tweet 104

    # Segui e smetti di seguire utenti
    twitter.follow(1, 2)  # Utente 1 segue l'utente 2
    twitter.follow(1, 3)  # Utente 1 segue l'utente 3
    twitter.unfollow(1, 3)  # Utente 1 smette di seguire l'utente 3

    # Recupera il feed
    feed = twitter.get_feed(1)  # Recupera il feed per l'utente 1
    print("Feed utente 1:", feed)  # Stampa il feed dell'utente 1