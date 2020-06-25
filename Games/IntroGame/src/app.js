//import Paddle from "./src/paddle";

class Paddle{
    constructor (gameWidth,gameHeight) {
        this.width = 150;
        this.height = 30;
        this.position = {
            x: gameWidth / 2 - this.width / 2,
            y: gameHeight - this.height-10
        }
    }
    draw(ctx){
        console.log('Funciona');
        ctx.fillStyle = '#0ff'
        ctx.fillRect(this.position.x,this.position.y,this.width,this.height)
    }
}


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


