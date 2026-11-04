
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Flask!</h1>
    <form action="/submit" method="POST">
        <input type="text" name="username"
               placeholder="Enter your name" required>
        <button type="submit">Submit</button>
    </form>
    """

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    return f"<h1>Hello, {username}!</h1>"

if __name__ == '__main__':
    app.run()
