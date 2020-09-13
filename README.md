# flask-csp

This repo contains incrementing modules on how to build a website in Flask.

## Installation
``` git clone https://github.com/nighthawkcoders/flask-csp ``` to get started.

Before you begin be sure to create a virtual enviornment within the flask-csp directory.
1. ```$ pip install virtualenv ```
2. ```$ python -m venv venv ```*

If you are on Windows...

```> source venv/Scripts/activate ``` 

If you are on MacOS/Linux...

```$ source venv/bin/activate ```

This will activate your virtual enviornment, you should now see a (venv) before your cursor.


To start a flask project navigate to your desired module in terminal (```"cd", "cd .."```)

install needed packages by running
```pip install -r requirements.txt ``` within your virtual enviornment. Most will be already be installed.

Finnally start the server with ```$ python run.py ```

*If you are on MacOS/Linux replace "python" with "python3"

***


## 001: The basics
- setting up a Flask server
- creating pages and displaying content

## 002: Adding more features
- Loading HTML from a seperate file
- Passing arguments through a url
- Using jinja to read variables from HTML

## 03: Creating an online store
- Dynamic url's in flask
- Jinja flow control and conditional statements
- Passing objects of data to be displayed
- Handling forms and user input (POST)

## 04: Improving online store
- Package structure and code delegations
- SQLite database using flask_sqlalchemy
- Using class inheritance and objects