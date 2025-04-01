## 🏆 Esercizio 2 - Scelta del Modello Copilot
### Obiettivo:
Confrontare l'output di diversi modelli di intelligenza artificiale (GPT-4, Claude, o1) per capire quale sia il più adatto in base al contesto.

### 📌 Esempio:
#### Prompt:
```python
# Scrivi una funzione Python chiamata is_valid_password che controlla se una password è sicura.
# - Deve avere almeno 8 caratteri
# - Deve contenere almeno una lettera maiuscola, una minuscola e un numero
# - Deve restituire True se la password è valida, altrimenti False
```

| Modello  | Output Atteso | Note |
|----------|--------------|------|
| **GPT-4** | ✅ Usa una regex avanzata e include test unitari. | Ottimo per codice robusto. |
| **Claude** | 🔶 Implementa `if` annidati senza regex. | Più leggibile ma meno efficiente. |
| **o1** | ❌ Output incompleto o errato. | Non consigliato per codice complesso. |