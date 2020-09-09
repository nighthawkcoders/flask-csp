from flask import Flask, render_template

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/hello/<name>')
def about(name):

    return render_template("hello.html", name=name)

@app.route('/weather')
def weather():

    # BONUS: return the current time as well
    time = datetime.now().time()
    #=======================================

    weather = {
        "temperature":"95°F",
        "percipitation":"4%",
        "wind_speed":3,
        "type":"fair",
        "time":time
    }

    return render_template("weather.html", weather=weather)


@app.route('/sum-api/<num1>/<num2>')
def sum_api(num1, num2):

    try: # The user might input a string
        result = {
            "function":"sum",
            "num1":num1,
            "num2":num2,
            "answer": int(num1) + int(num2)
            }

        return result

    except Exception as e:
        error_message = {
            "function":"sum",
            "num1":num1,
            "num2":num2,
            "error":str(e)
        }

        return error_message

    return # Should never get here because it either passes in try or fails to except






if __name__ == "__main__":
    app.run(debug=True)