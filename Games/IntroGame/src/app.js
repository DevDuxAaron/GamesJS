import Paddle from "./src/paddle";

// Obteniendo el canvas
let canvas = document.getElementById("gameScreen");
let ctx = canvas.getContext("2d");

// // Coloreando el canvas
// ctx.fillStyle = '#d0e   '
// ctx.fillRect(20,20,100,100)

// ctx.fillStyle = '#0ee'
// ctx.fillRect(150,150,60,60)

// Limpiando el canvas
// Requiere area de limpiado
// ctx.clearRect(0,0,800,600)

const GAME_WIDTH = 800
const GAME_HEIGHT = 600

// ctx.clearRect(0,0,800,600)

let paddle = new Paddle(GAME_WIDTH,GAME_HEIGHT);

paddle.draw(ctx)