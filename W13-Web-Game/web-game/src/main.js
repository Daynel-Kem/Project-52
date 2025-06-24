import kaplay from "kaplay";
// import "kaplay/global"; // uncomment if you want to use without the k. prefix

const scale = 2;

const k = kaplay({
    width: 640 * scale,
    height: 360 * scale,
    global: false,
    letterbox: true,
    scale,
});

k.loadRoot("./"); // A good idea for Itch.io publishing later

k.