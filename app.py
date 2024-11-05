from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    UserDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    computer = random.choice([-1, 0, 1])
    User = UserDict[user_choice]

    result_message = ""
    result_color = ""

    if computer == User:
        result_message = "It's a draw!"
        result_color = "blue"
    elif (computer == -1 and User == 1) or (computer == 0 and User == -1) or (computer == 1 and User == 0):
        result_message = "You win!"
        result_color = "green"
    else:
        result_message = "You lose!"
        result_color = "red"

    return render_template('results.html', 
                           user_choice=reverseDict[User], 
                           computer_choice=reverseDict[computer], 
                           result_message=result_message,
                           result_color=result_color)

if __name__ == '__main__':
    app.run(debug=True)