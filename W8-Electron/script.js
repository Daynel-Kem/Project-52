async function changeText() {
    const information = document.getElementById("text")
    await fetch(api)
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

    const textBox = document.querySelector('.textbox');
    const eg = document.getElementById('eg')
    
    
    textBox.style.opacity = 1;
    eg.src = './assets/eg_talk.gif'

    setTimeout(() => {
        textBox.style.opacity = 0;
        eg.src = './assets/eg.gif'
    }, 6000)
}