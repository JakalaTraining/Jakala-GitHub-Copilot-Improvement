# Esercizio di Debugging: LRU Cache

## Obiettivo
Identificare e correggere un bug nel codice della LRU Cache.

## Traccia
Ti viene fornita un'implementazione della classe `LRUCache` che dovrebbe rispettare le specifiche di una cache Least Recently Used (LRU). Tuttavia, presenta alcuni bug che impediscono il corretto funzionamento.

## Passaggi:
1. Analizza il codice fornito di seguito inserendo dei commenti e prova a capire dove si trova l’errore.
2. Correggi i bug e spiega la modifica apportata.
3. Verifica che la cache si comporti correttamente eseguendo i test forniti:

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

# Esercizio di Generazione di Test: LRU Cache

## Obiettivo
Generare test per verificare il corretto funzionamento della classe LRU Cache.

## Traccia
Ti viene fornita un'implementazione della classe `LRUCache` che dovrebbe rispettare le specifiche di una cache Least Recently Used (LRU). Il tuo compito è generare test per verificare che la cache si comporti correttamente in vari scenari.

## Passaggi:
1. Analizza il codice fornito di seguito e identifica i casi di test necessari per verificare il corretto funzionamento della cache.
2. Scrivi i test per ciascun caso identificato.
3. Esegui i test e verifica che i risultati siano corretti.

## Esempi:
Genera test unitari per la classe LRUCache utilizzando. I test dovrebbero verificare:
1. L'inserimento e il recupero di valori.
2. La rimozione del nodo meno usato quando la cache è piena.
3. L'aggiornamento del valore di una chiave esistente.
4. L'aggiornamento dell'ordine dei nodi quando una chiave viene acceduta.
5. Il comportamento della cache quando la capacità è 1.

## Domande:
1. I test coprono tutti i possibili scenari di utilizzo della LRU Cache? Se no, quali altri test aggiungeresti?
2. Se dovessi migliorare la tua implementazione, cosa cambieresti per rendere il codice più robusto?
3. Se la cache fosse usata in un sistema ad alto carico, quali ottimizzazioni potresti implementare?