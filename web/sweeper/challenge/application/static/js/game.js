let game_over = false;
let winner = false;
let board = $("#board");

const downloadFile = (filename,text) => {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

const setupBoard = (config) => {
    let width = config.width;
    let height = config.height;
    board.html("");
    for(y=0; y<width; y++) {
        row = $("<tr></tr>");
        for(x=0; x<height; x++) {
            row.append("<td class='board_cell' data-y='"+y+"' data-x='"+x+"'></td>");
        }
        board.append(row);
    }

    $('.board_cell').mouseup(function(event) {
        if(event.which == 3)
            clickCell($(this),"flag");
        else
            clickCell($(this),"click");
    });
};

// Detect if service is running on https
let wsProtocol = 'ws://';
if (window.location.protocol === 'https:') {
    wsProtocol = 'wss://';
}

// Open connection to game backend
const socket = new WebSocket(wsProtocol + location.host + '/game');

let ping_int = window.setInterval(function(){
    socket.send(JSON.stringify({message_type:"ping"}));
},20000);

socket.onerror = function (evt) {
    $("#messageModalTitle").html("Connection Lost");
    $("#messageModalBody").html("The connection to the game server was lost. Please reload the page to start a new game.");
    $("#messageModal").modal('show');
    window.clearInterval(ping_int);
};

const clickCell = (cell,click_type) => {
    if(game_over || cell.hasClass("cleared"))
    return;

    socket.send(JSON.stringify({message_type:click_type,x:cell.data("x"),y:cell.data("y")}));
}

const resetCell = (cell) => {
    cell.html("");
    cell.removeClass();
    cell.addClass("board_cell");
}

const updateBoard = (board) => {
    for (x=0; x<board.length; x++) {
        for(y=0; y<board[x].length; y++) {
            update = board[x][y];

            cell = $("td[data-x='"+x+"'][data-y='"+y+"']");

            resetCell(cell);

            if(update.cleared){
                cell.addClass("cleared");
                if(update.nearby > 0) {
                    cell.addClass("nearby-"+update.nearby);
                    cell.html(update.nearby);
                }
            } else if (update.flagged) {
                if (game_over && !update.mine)
                    cell.addClass("wrong_mine");
                else
                    cell.addClass("flagged");
            } else if (game_over && update.mine) {
                cell.addClass("mine");
                if (!winner)
                cell.addClass("loser");
            }
        }
    }
};

const handleGameState = (state) => {
    game_over = state.game_over;
    winner = state.winner;
    $("#bomb-counter").html(state.mines - state.flagged);
    updateBoard(state.board);
    if(game_over)
    console.log("Game Over! Winner = "+winner);
};

const handleModal = (message) => {
    $("#messageModalTitle").html(message.title);
    $("#messageModalBody").html(message.body);
    $("#messageModal").modal('show');
};

socket.addEventListener('message', ev => {
    try {
        data = JSON.parse(ev.data);

        switch(data.message_type){
            case 'message':
                console.log(data.message);
                break;
            case 'game_config':
                setupBoard(data.message);
                break;
            case 'game_state':
                handleGameState(data.message);
                break;
            case 'modal':
                handleModal(data.message);
                break;
            case 'save':
                downloadFile("sweeper.save",data.message);
                break;
            default:
                console.log(data);
                break;
        }

    } catch (e) {
        console.log("Unable to parse message from server");
        console.log(e);
    }
});

$(document).ready(function(){
    //Don't allow right-click
    $('#content').contextmenu(function(event) {
        event.preventDefault();
    });

    $("#reset_button").click(function(){
        socket.send(JSON.stringify({message_type:"reset"}));
    });

    $("#save_button").click(function(){
        socket.send(JSON.stringify({message_type:"save"}));
    });

    $("#load_button").click(function(){
        $("#loadModal").modal('show');
    });

    $("#credits_button").click(function(){
        $("#creditsModal").modal('show');
    });

    $("#loadFile").change(function(){
        let fr = new FileReader();
        fr.onload=function(){
            socket.send(JSON.stringify({message_type:"load","state":fr.result}));
            $("#loadModal").modal('hide');
        }
        fr.readAsText(this.files[0]);
    });
});