
from flask import Flask, render_template, jsonify, request
from game import Game

x=20
y=20
app = Flask(__name__)
board = Game(x, y)


# Display Frontend
@app.route('/')
def home():
    return render_template('page.html')

# Backend Routes
@app.route('/api/get_state')
def get_data():
    return jsonify(board.gameBoard)

@app.route('/api/next_gen', methods=['POST'])
def next_gen():
    board.nextGen(1)
    return jsonify(success=True)

@app.route('/api/toggle', methods=['POST'])
def toggle():
    data = request.json
    row, col = data['row'], data['col']
    board.toggle((col, row))
    return jsonify(success=True)

@app.route('/api/special', methods=['POST'])
def special():
    board.special()
    return jsonify({'x': board.specialx,
                    'y': board.specialy})

@app.route('/api/reset', methods=['POST'])
def reset():
    board.reset()
    return jsonify(success=True)


if __name__ == '__main__':
    app.run()
