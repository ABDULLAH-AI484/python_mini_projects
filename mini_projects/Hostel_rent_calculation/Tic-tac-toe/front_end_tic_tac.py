from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the game board and current player
board = ["", "", "", "", "", "", "", "", ""]
current_player = "X"

# Winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

@app.route("/")
def index():
    return render_template("index.html", board=board, current_player=current_player)

@app.route("/move/<int:index>")
def move(index):
    global board, current_player

    # Check if the cell is empty
    if board[index] == "":
        # Update the board with the current player's move
        board[index] = current_player

        # Check for a winner
        if check_winner():
            return redirect(url_for("result", winner=current_player))
        # Check for a tie
        elif "" not in board:
            return redirect(url_for("result", winner="tie"))
        # Switch players
        else:
            current_player = "O" if current_player == "X" else "X"
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route("/reset")
def reset():
    global board, current_player
    # Reset the board and current player
    board = ["", "", "", "", "", "", "", "", ""]
    current_player = "X"
    return redirect(url_for("index"))

@app.route("/result/<winner>")
def result(winner):
    return render_template("result.html", winner=winner, board=board)

def check_winner():
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return True
    return False

if __name__ == "__main__":
    app.run(debug=True)