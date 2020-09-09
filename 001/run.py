from flask import Flask, render_template

app = Flask(__name__)

# http://localhost:5000/
@app.route('/')
def home():
    return "Hello World! from my website"

# http://localhost:5000/about
@app.route('/about')
def about():
    return """
    <h1>About Page goes here</h1>
    <p> This is some placeholder text for the about page </p>
    """

# http://localhost:5000/data
@app.route('/data')
def data():
    my_data = {"age":16, "weather":"100C", "language":"python"}
    return my_data


if __name__ == "__main__":
    app.run(debug=True)