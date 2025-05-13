// Funzione per la gestione del form "Tesserati - Inserisci Nuovo"
document.getElementById('tesserati-form').addEventListener('submit', function (e) {
  e.preventDefault();

  // Raccolta dei dati dal form
  const form = e.target;
  const dati = {
    cognome: form.cognome.value.trim(),
    nome: form.nome.value.trim(),
    indirizzo: form.indirizzo.value.trim(),
    citta: form.citta.value.trim(),
    password: form.password.value,
    dataNascita: form.dataNascita.value,
    cap: form.cap.value.trim(),
    telefono: form.telefono.value.trim(),
    email: form.email.value.trim(),
    numDocumento: form.numDocumento.value.trim(),
    tipoDocumento: form.tipoDocumento.value,
  };

  // Validazione semplice (può essere estesa)
  let errori = [];
  if (!dati.cognome) errori.push("Il campo Cognome è obbligatorio.");
  if (!dati.nome) errori.push("Il campo Nome è obbligatorio.");
  if (!dati.email) errori.push("Il campo E-mail è obbligatorio.");
  if (!dati.password) errori.push("Il campo Password è obbligatorio.");

  if (errori.length > 0) {
    alert(errori.join('\n'));
    return;
  }

  // Simula il salvataggio dei dati
  alert('Dati inseriti correttamente:\n' + JSON.stringify(dati, null, 2));
  form.reset();
});

// Pulsante "Resetta" resetta il modulo (comportamento standard)
// Pulsante "Esci" mostra conferma uscita
document.querySelector('.exit-btn').addEventListener('click', function () {
  if (confirm('Vuoi davvero uscire?')) {
    // Simula la chiusura dell'applicazione
    window.location.reload();
  }
});

// Sidebar: evidenzia il pulsante attivo al click
document.querySelectorAll('.sidebar-buttons button').forEach(btn => {
  btn.addEventListener('click', function () {
    document.querySelectorAll('.sidebar-buttons button').forEach(el => el.classList.remove('active'));
    btn.classList.add('active');
    // Simula il cambio sezione
    alert('Sezione "' + btn.innerText + '" non implementata in questa demo.');
  });
});