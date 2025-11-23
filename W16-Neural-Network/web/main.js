const grid = document.getElementById("grid")
const clearButton = document.getElementById("clear")
const submitButton = document.getElementById("submit")
let isMouseDown = false

for (let i = 0; i < 100; ++i) {
    button = document.createElement("button")
    button.classList.add("button")
    button.id = `${i}`
    grid.appendChild(button)
}

document.addEventListener("mousedown", (e) => {
    if (e.button === 0) isMouseDown = true;
})

document.addEventListener("mouseup", () => {
    isMouseDown = false;
})

function toggleButton(e) {
  e.target.classList.toggle("active");
}

document.querySelectorAll(".button").forEach(button => {
    button.addEventListener("click", toggleButton);

    button.addEventListener("mouseenter", () => {
        if (isMouseDown) {
            toggleButton({target: button});
        }
    })
})

function clear() {
    document.querySelectorAll(".button").forEach(button => {
        button.classList.remove("active")
    })
}

clearButton.addEventListener("click", clear)

function checkShape() {
    shape = []
    for (let i = 0; i < 100; i++) {
        button = document.getElementById(i)
        if (button.classList.contains("active")) {
            shape[i] = 1
        } else {
            shape[i] = 0
        }
    }
    console.log(shape)
}

submitButton.addEventListener("click", checkShape)



