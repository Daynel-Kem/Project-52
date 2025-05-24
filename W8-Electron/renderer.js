const api = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
const information = document.getElementById("text")
fetch(api)
.then(response => {
    if (!response.ok) {
        throw new Error("network response was not ok");
    }
    return response.json();
})
.then(data => {
    information.innerText = data.text;
})
.catch(error => {
    console.log('Fetch error', error)
})