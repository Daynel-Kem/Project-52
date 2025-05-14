const foo = (name) => {
    if (name != "John") {
        return "Hello, " + name;
    } else {
        return "What's good John?";
    }
}

module.exports = {foo}