document.addEventListener("DOMContentLoaded", () => {
  //card optiions
  const cardArray = [
    {
      name: "blue",
      img: "images/puzzlepack/png/element_blue_square.png",
    },
    {
      name: "green",
      img: "images/puzzlepack/png/element_green_square.png",
    },
    {
      name: "purple",
      img: "images/puzzlepack/png/element_purple_square.png",
    },
    {
      name: "red",
      img: "images/puzzlepack/png/element_red_square.png",
    },
    {
      name: "yellow",
      img: "images/puzzlepack/png/element_yellow_square.png",
    },
    {
      name: "blue",
      img: "./images/puzzlepack/png/element_blue_square.png",
    },
    {
      name: "green",
      img: "images/puzzlepack/png/element_green_square.png",
    },
    {
      name: "purple",
      img: "images/puzzlepack/png/element_purple_square.png",
    },
    {
      name: "red",
      img: "images/puzzlepack/png/element_red_square.png",
    },
    {
      name: "yellow",
      img: "images/puzzlepack/png/element_yellow_square.png",
    },
    {
      name: "red",
      img: "images/puzzlepack/png/element_red_square.png",
    },
    {
      name: "red",
      img: "images/puzzlepack/png/element_red_square.png",
    }
  ];

  cardArray.sort(() => 0.5 - Math.random());

  const grid = document.querySelector(".grid");
  const resultDisplay = document.querySelector("#result");
  var cardsChosen = [];
  var cardsChosenId = [];
  var cardsWon = [];

  function createBoard() {
    for (let i = 0; i < cardArray.length; i++) {
      var card = document.createElement("img");
      card.setAttribute(
        "src",
        "./images/puzzlepack/png/element_grey_square_glossy.png"
      );
      card.setAttribute("data-id", i);
      card.addEventListener("click", flipCard);
      grid.appendChild(card);
    }
  }

  //check for match
  function checkForMatch() {
    var cards = document.querySelectorAll("img");
    const optionOneId = cardsChosenId[0];
    const optionTwoId = cardsChosenId[1];
    if (cardsChosen[0] === cardsChosen[1] && cardsChosenId[0] != cardsChosenId[1]) {
      //alert("You found a match");
      cards[optionOneId].setAttribute(
        "src",
        "./images/alertita.png"
      );
      cards[optionOneId].setAttribute(
        "width",
        "32px"
      );
      cards[optionOneId].setAttribute(
        "height",
        "32px"
      );
      cards[optionTwoId].setAttribute(
        "src",
        "./images/alertita.png"
      );
      cards[optionTwoId].setAttribute(
        "width",
        "32px"
      );
      cards[optionTwoId].setAttribute(
        "height",
        "32px"
      );
      cardsWon.push(cardsChosen);
    } else {
      cards[optionOneId].setAttribute(
        "src",
        "./images/puzzlepack/png/element_grey_square_glossy.png"
      );
      cards[optionTwoId].setAttribute(
        "src",
        "./images/puzzlepack/png/element_grey_square_glossy.png"
      );
      //alert("Sorry");
    }
    cardsChosen = [];
    cardsChosenId = [];
    resultDisplay.textContent = cardsWon.length;
    if (cardsWon.length === cardArray.length / 2) {
      resultDisplay.textContent = "Ganaste el juego con una puntuacion de " + cardsWon.length;
    }
  }

  //flip your card
  function flipCard() {
    var cardId = this.getAttribute("data-id");
    cardsChosen.push(cardArray[cardId].name);
    cardsChosenId.push(cardId);
    this.setAttribute("src", cardArray[cardId].img);
    if (cardsChosen.length === 2) {
      setTimeout(checkForMatch, 500);
    }
  }

  createBoard();
});
