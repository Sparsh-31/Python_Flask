
#Description
# Create a simple Flask application with the following specifications:

# - It should have at least three routes: **`/`**, **`/greet/<username>`**, and **`/farewell/<username>`**.
#     - **`/`** should display a welcome message.
#     - **`/greet/<username>`** should display a greeting message for the user specified in **`<username>`**. For example, if you navigate to **`/greet/John`**, it should display "Hello, John!".
#     - **`/farewell/<username>`** should display a farewell message for the user specified in **`<username>`**. For example, if you navigate to **`/farewell/John`**, it should display "Goodbye, John!".


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome!"

@app.route('/greet/<username>')
def greet(username):
    return f"Hello, {username}!"

@app.route('/farewell/<username>')
def farewell(username):
    return f"Goodbye, {username}!"

if __name__ == '__main__':
    app.run()