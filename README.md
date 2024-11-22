# Snake, Water, Gun Game with Flask 🎮

Welcome to the **Snake, Water, Gun Game**! This simple web-based game is built using **Python** and **Flask**, where you play against the computer in a classic game of **Snake 🐍**, **Water 💧**, and **Gun 🔫**. May the best choice win! 🚀

## Table of Contents
- [Introduction](#introduction)
- [How to Run the Project](#how-to-run-the-project)
- [Project Structure](#project-structure)
- [Code Explanation](#code-explanation)
- [Technologies Used](#technologies-used)
- [Contribute](#contribute)

---

## Introduction

This is a fun and simple **Snake, Water, Gun** game where you select one of the three choices, and the computer makes a random choice. Then, the winner is determined based on the following rules:
- **Snake 🐍** beats **Water 💧**
- **Water 💧** beats **Gun 🔫**
- **Gun 🔫** beats **Snake 🐍**

### Features:
- **Play against the computer** 🤖
- **Color-coded feedback** to show if you won, lost, or drew.
- Simple and easy-to-understand interface 🌟
- Responsive design, works well on both **desktop** and **mobile** devices 📱💻

---

## How to Run the Project

To get started, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/snake-water-gun-game.git
    ```

2. **Install Dependencies**:
    Make sure you have **Python** installed. Then, create a virtual environment and install the required dependencies:
    ```bash
    cd snake-water-gun-game
    python3 -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    Start the Flask application:
    ```bash
    python app.py
    ```

4. Open your browser and visit `http://127.0.0.1:5000` to start playing the game! 🎮

---

## Project Structure

### `app.py`

This file contains the main **Flask** application with the logic for the game. It handles:
- The home page (`/`), where users can choose between **Snake**, **Water**, or **Gun**.
- The `/play` route, which processes the user input and compares it to the computer’s random choice.

```python
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
```

### `templates/index.html`

This file contains the front-end HTML code for the game’s user interface. It displays the game options and interacts with the backend.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snake, Water, Gun Game</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        .result-message {
            font-size: 1.5em;
            margin-top: 20px;
        }
        .btn-primary {
            background-color: #6200ea;
            border-color: #6200ea;
        }
        .btn-primary:hover {
            background-color: #3700b3;
            border-color: #3700b3;
        }
    </style>
</head>
<body>
    <div class="container text-center">
        <h1>Snake, Water, Gun Game 🎮</h1>
        <div class="row justify-content-center">
            <div class="col-md-6">
                <form action="/play" method="POST">
                    <div class="btn-group">
                        <button type="submit" name="choice" value="s" class="btn btn-primary">Snake 🐍</button>
                        <button type="submit" name="choice" value="w" class="btn btn-primary">Water 💧</button>
                        <button type="submit" name="choice" value="g" class="btn btn-primary">Gun 🔫</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
```

---

## Technologies Used

- **Python**: Backend programming language used for the app logic.
- **Flask**: Web framework for Python to handle routing and rendering templates.
- **HTML/CSS**: Used to build the structure and style the game interface.
- **Bootstrap**: For responsive design and easy styling.
- **JavaScript (Optional)**: Used for any dynamic features (if added in the future).

---

## Contribute

We welcome contributions! Feel free to fork the repository, open an issue, or submit a pull request for improvements or bug fixes. 😊



**Enjoy playing the game and happy coding!** 🎉🚀


### Highlights of this README:
- **Clear Structure**: Sections like **Introduction**, **How to Run**, **Project Structure**, and more are broken down for easy reading.
- **Emojis**: Used strategically to add a fun and engaging touch.
- **Step-by-Step Instructions**: Easy-to-follow commands for setup and running the game.
- **Interactive Game Features**: Key game logic and features are well explained.
