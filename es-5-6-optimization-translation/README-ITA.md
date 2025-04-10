# 🔁 ESERCIZIO 5: Adattabilità tra Linguaggi di Programmazione

## 🆚 Confronto tra la versione **C#** e la versione **JavaScript**

### ✅ Obiettivo
Tradurre e analizzare una classe `Twitter` da C# in JavaScript, valutando:
- Differenze sintattiche e semantiche
- Strutture dati alternative
- Implicazioni sulle performance
- Strategia di adattamento

---

## 1. 📦 Strutture Dati Utilizzate

| C#                           | JavaScript                    |
|-----------------------------|-------------------------------|
| `Dictionary<int, List<>>`   | `Map<number, Array<>>`        |
| `HashSet<int>`              | `Set<number>`                 |
| `List<(int, int)>`          | `Array<[number, number]>`     |
| `PriorityQueue`             | `Manual Heap / Array + sort`  |

JavaScript non ha una `PriorityQueue` nativa, ma si può simulare:
- Con librerie esterne (`heap.js`)
- Con un array ordinato (approccio più semplice per esercizi)

---

## 2. 🔄 Traduzione Concettuale della Logica

### 📥 `postTweet(userId, tweetId)`
- C#: aggiunge alla lista, ordina per timestamp decrescente
- JS: `this.count--` crea timestamp negativi → più recente = più basso

### 📰 `getNewsFeed(userId)`
- C#: Usa `PriorityQueue` per combinare tweet propri e dei seguiti
- JS: Necessita implementazione alternativa (heap manuale o array ordinato)

### ➕➖ `follow()` / `unfollow()`
- C#: usa un dizionario `Dictionary<int, HashSet<int>>`
- JS: `Map<number, Set<number>>` per simularlo

---

## 3. ⏱️ Analisi della Complessità Temporale

**Obiettivo della funzione `getNewsFeed`:**
Restituire i 10 tweet più recenti dell’utente e di chi segue.

### ✅ Complessità attesa:
- Itera su utenti seguiti (n): `O(n)`
- Inserisce max 10 tweet per utente in un heap: `O(n log k)` con `k = n × 10`
- Estrae 10 tweet: `O(10 log k)` → costante

➡️ **Risultato:** `O(n log n)` con `c=10` come costante

---

## 4. 🔧 Implementazione JavaScript della Classe Twitter

```javascript
class Twitter {
  constructor() {
    this.tweetMap = new Map();        // userId → Array<[timestamp, tweetId]>
    this.followMap = new Map();       // userId → Set<userId>
    this.count = 0;                   // Simula timestamp
  }

  postTweet(userId, tweetId) {
    if (!this.tweetMap.has(userId)) {
      this.tweetMap.set(userId, []);
    }
    this.tweetMap.get(userId).push([this.count--, tweetId]);
    if (this.tweetMap.get(userId).length > 10) {
      this.tweetMap.get(userId).shift();  // Rimuove il più vecchio
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

    // Include i propri tweet
    if (this.tweetMap.has(userId)) {
      tweets.push(...this.tweetMap.get(userId));
    }

    // Include i tweet degli utenti seguiti
    const followees = this.followMap.get(userId) || new Set();
    for (const followeeId of followees) {
      if (this.tweetMap.has(followeeId)) {
        tweets.push(...this.tweetMap.get(followeeId));
      }
    }

    // Ordina per timestamp decrescente (più recenti prima)
    tweets.sort((a, b) => a[0] - b[0]);

    // Restituisce solo gli ultimi 10 tweetId
    return tweets.slice(0, 10).map(([_, tweetId]) => tweetId);
  }
}
```

---

## 5. 🧠 Osservazioni Finali e Best Practices

### 📌 Simulazione Heap
Per un confronto fedele con C#, si potrebbe sostituire il sort con un heap binario esplicito.

### 📌 Gestione Edge Case
- Utente che non ha postato → `tweetMap.get()` restituisce `undefined`
- Utente che non segue nessuno → `followMap.get()` restituisce `Set` vuoto

---

## 6. ✍️ Suggerimenti per Prompt ed Estensioni Future

Quando chiedi a Copilot simili:
> ✨ "Implementa la funzione `getNewsFeed()` in JavaScript in modo che ritorni i 10 tweet più recenti di un utente e dei suoi followee, usando un heap (o simulazione) per mantenere l’ordine temporale."

Altri prompt efficaci:
- "Limita i tweet a 10 per utente e ordina in ordine decrescente di tempo."
- "Gestisci follow/unfollow usando `Map` e `Set`."
- "Implementa una `PriorityQueue` per simulare la struttura C# nativa."

---

# ESERCIZIO 6: Analisi degli Output di GitHub Copilot Chat

## Correttezza dell'analisi di complessità

Senza vedere l'implementazione completa di `getNewsFeed()` nella classe C# originale, è difficile valutare con certezza la correttezza dell'analisi. Tuttavia, l'analisi di Copilot "O(n log k)" per il caso peggiore sembra plausibile considerando:

1. La necessità di iterare su tutti gli utenti seguiti (componente "n")
2. L'utilizzo di un heap (PriorityQueue) per mantenere e selezionare i tweet più recenti (componente "log k")

## Significato di n e k

Copilot definisce:
- n = numero di utenti seguiti
- k = numero massimo di tweet (fino a 10 per utente)

Questa definizione è parzialmente corretta, ma imprecisa:
- **n** è correttamente identificato come il numero di utenti seguiti
- **k** non è propriamente definito. Un'interpretazione più accurata sarebbe: k è il numero totale di tweet considerati (che può arrivare fino a n×10, dove 10 è il limite di tweet per utente)

## Influenza del limite di 10 tweet sulla complessità

Il limite di 10 tweet per utente ha un impatto significativo sulla complessità:

1. **Riduzione della dimensione dell'heap**: L'heap conterrà al massimo n×10 elementi (non tutti i tweet della piattaforma)

2. **Tempo di esecuzione costante** per le operazioni con ciascun utente: il numero di tweet processati per utente è limitato, quindi le operazioni per utente sono O(1) invece che O(numero totale di tweet dell'utente)

3. **Complessità effettiva**: Poiché il limite di 10 è una costante, la complessità può essere espressa come O(n log n) anziché O(n log k), dato che k ≤ 10n, quindi log k è dell'ordine di log n più una costante.

## Versione migliorata della spiegazione

Una spiegazione più precisa della complessità temporale di `getNewsFeed()` sarebbe:

"La complessità temporale di getNewsFeed() è O(n log(n×c)), dove:
- n è il numero di utenti seguiti
- c è il limite costante di tweet per utente (10 in questo caso)

Il processo può essere suddiviso in:
1. Iterazione su ciascuno degli n utenti seguiti: O(n)
2. Per ogni utente, estrazione dei suoi tweet recenti (limitati a 10): O(1) per utente
3. Inserimento di questi tweet in un heap di dimensione massima n×10: ogni inserimento costa O(log(n×10))
4. Estrazione dei 10 tweet più recenti dall'heap: O(10 log(n×10))

Poiché c=10 è una costante, la complessità può essere semplificata a O(n log n).

Il passaggio più costoso è la gestione dell'heap durante il merge dei tweet provenienti da utenti diversi, che richiede operazioni di ordinamento logaritmiche rispetto alla dimensione dell'heap."

--- 