async function submitNote() {
    const text = document.getElementById('input').value;
    await fetch('http://localhost:5000/api/notes', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ text })
    });
    document.getElementById('input').value = '';
    loadNotes();
}

async function loadNotes() {
    const res = await fetch('http://localhost:5000/api/notes');
    const notes = await res.json();
    const table = document.getElementById('board');
    table.innerHTML = '';
    notes.forEach(([id, text]) => {
        table.innerHTML += `<tr><td>${id}</td><td>${text}</td></tr>`;
    });
}

loadNotes();