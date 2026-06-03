# What is Flask
# Flask is a micro Web framework written in python
# Flask is a library

# Flask Concept :
#Browser (Chorme) --> request --> Flask --> Python code
#Browser (Chorme) <-- response <-- Flask <-- Python code

#@app.route('/') --> This handle URL
#def home(): --> This is function
#return... -->This is take to browser


#Web ApplicationS

import html
from turtle import ht

from flask import Flask, app
app = Flask(__name__)
# project data - dictionary
students = [
    {
        "name" : "Ram",
        "marks" : "85"
    },
    {
        "name" : "Kartik",
        "marks" : "75"
    },
    {
        "name" : "Karan",
        "marks" : "77"
    }
]

@app.route('/')
def home():
    # Create using HTML
    html = '<h1>Collage Portal - Students </h1>'
    html +='<ul>'

    for student in students:
        html += f'<li>{student["name"]}: {student["marks"]}</li>'

    html += '</ul>'
    return html

@app.route('/about')
def about():
    return '<h1>This is a collage management System</h1>'

@app.route('/student')
def student():
    return '<h1>All Student show here</h1>'

if __name__ =='__main__':
    app.run(debug=True)
