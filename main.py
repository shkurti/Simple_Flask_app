# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 20:31:13 2021

@author: Gladiator7
"""

from flask import Flask

app = Flask(__name__)



@app.route("/")
def home():
    return "Hello! this is the main page <h1>HELLO<h1>"

@app.route("/<name>")
def user(name):
    print(name)
    return f"HELLO {name}!"

# if __name__ == '__main__':
#     app.run(port=5000,debug=True)
if __name__ == '__main__':
   app.run(debug=False,host='0.0.0.0')   