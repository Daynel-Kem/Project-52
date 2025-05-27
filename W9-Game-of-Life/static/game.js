const gridEl = document.getElementById("grid");

function createGrid(state) {
    gridEl.innerHTML = '';
    state.forEach((row, r) => {
        row.forEach((cell, c) => {
            const div = document.createElement("div");
            div.classList.add("cell");
            if (cell === 1) div.classList.add("alive");
            div.addEventListener("click", () => toggleCell(r, c));
            gridEl.appendChild(div);
        });
    });
}

function fetchState() {
    fetch('/api/get_state')
        .then(res => res.json())
        .then(data => createGrid(data));
}

function step() {
    fetch('/api/next_gen', { method: 'POST' })
        .then(() => fetchState());
}

function toggleCell(row, col) {
    fetch('/api/toggle', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ row, col })
    }).then(() => fetchState());
}

function reset() {
    fetch('/api/reset', {
        method: 'POST'
    }).then(() => fetchState())
}

fetchState();
