$(document).ready(function(){

let gameId = "";
let nextLetter = 0;
let currentGuess = [];
let gameOver = false;
let row = document.getElementsByClassName("letter-row")[0];

function insertLetter (pressedKey) {
    if (nextLetter === 5) {
        return
    }
    pressedKey = pressedKey.toLowerCase();
    let box = row.children[nextLetter];
    box.textContent = pressedKey;
    box.classList.add("filled-box");
    currentGuess.push(pressedKey);
    nextLetter += 1;
}

function deleteLetter () {
    let box = row.children[nextLetter - 1];
    box.textContent = "";
    box.classList.remove("filled-box");
    currentGuess.pop();
    nextLetter -= 1;
}

function colorLetters(correct) {
    for (var i = 0; i < 5; i++) {
        let box = row.children[i];
        if (currentGuess[i] == correct.charAt(i)) {
            box.classList.add("green");
        } else if (correct.includes(currentGuess[i])) {
            box.classList.add("yellow");
        } else {
            box.classList.add("grey");
        }
    }
}

function clearGuess (){
    Array.from(row.children).forEach((box) => {
        box.textContent = "";
        box.classList.remove("filled-box");
        box.classList.remove("green");
        box.classList.remove("yellow");
        box.classList.remove("grey");
    });
    currentGuess = [];
    nextLetter = 0;
}


const getGame = async() => {

    let card = $("#resp-msg");

    await fetch(`/api/game`, {
        method: 'GET',
    })
    .then((response) => response.json()
        .then((resp) => {
            if (response.status == 200) {
                gameId = resp.game_id;
                return;
            }
        }))
    .catch((error) => {
        card.text("Error fetching new game.");
        card.attr("class", "alert alert-danger");
        card.show();
    });
}

const checkGuess = async() => {

    let card = $("#resp-msg");
	card.attr("class", "alert alert-info");
	card.text("Sending guess...");
	card.show();

    let guessString = '';

    for (const val of currentGuess) {
        guessString += val;
    }

    if (guessString.length != 5) {
        card.text("Not enough letters!");
        card.attr("class", "alert alert-danger");
        card.show();
        return;
    }
    
    await fetch(`/api/guess`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({guess: guessString, game_id: gameId}),
        credentials: 'same-origin',
    })
    .then((response) => response.json()
        .then((resp) => {
            if (response.status == 200) {
                gameOver = true;
                $("#resetButton").show();
                colorLetters(resp.correct_word);
                gameId = resp.game_id;
                card.attr("class", "alert alert-info");
                card.html(resp.message);
                card.show();
                return;
            }
            card.text(resp.error);
            card.show();
        }))
    .catch((error) => {
        clearGuess();
        card.text(error);
        card.attr("class", "alert alert-danger");
        card.show();
    });

    $('#submit').prop('disabled', false);
}

$("#resetButton").click(function(){
    gameOver = false;
    $(this).hide();
    clearGuess();
});

document.addEventListener("keyup", (e) => {

    if (gameOver) {
        return
    }

    let pressedKey = String(e.key)
    if (pressedKey === "Backspace" && nextLetter !== 0) {
        deleteLetter()
        return
    }

    if (pressedKey === "Enter") {
        checkGuess()
        return
    }

    let found = pressedKey.match(/[a-z]/gi)
    if (!found || found.length > 1) {
        return
    } else {
        insertLetter(pressedKey)
    }
});

document.getElementById("keyboard-cont").addEventListener("click", (e) => {

    if (gameOver) {
        return
    }


    const target = e.target
    
    if (!target.classList.contains("keyboard-button")) {
        return
    }
    let key = target.textContent

    if (key === "Del") {
        key = "Backspace"
    } 

    document.dispatchEvent(new KeyboardEvent("keyup", {'key': key}))
});

getGame();

});