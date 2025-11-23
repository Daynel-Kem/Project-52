const grid = document.getElementById("grid")
const clearButton = document.getElementById("clear")
const submitButton = document.getElementById("submit")
const prediction = document.getElementById("prediction")
const confidence = document.getElementById("confidence")
let isMouseDown = false

const backend_route = "https://neuralnetwork-seven.vercel.app"

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

async function checkShape() {
    shape = []
    for (let i = 0; i < 100; i++) {
        button = document.getElementById(i)
        if (button.classList.contains("active")) {
            shape[i] = 1
        } else {
            shape[i] = 0
        }
    }
    try {
        const data = {
            shape: shape,
        }
        const response = await fetch(`${backend_route}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
        }
        const result = await response.json()

        prediction.textContent = result.prediction
        confidence.textContent = `[Rectangle: ${result.Confidence[0][0].toFixed(3)}, Circle: ${result.Confidence[0][1].toFixed(3)}, Triangle: ${result.Confidence[0][2].toFixed(3)}]`;


        console.log(result)
    } catch (error) {
        console.error("Error Getting Prediction")
    }

    console.log(shape)
}

submitButton.addEventListener("click", checkShape)



