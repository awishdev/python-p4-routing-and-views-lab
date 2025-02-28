#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    the_string = ''
    for i in range(parameter):
        the_string += f'{i}\n'

    return the_string

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def math(num1, operator, num2):
    if operator == '+':
        return f'{num1 + num2}'
    elif operator == '-':
        return f'{num1 - num2}'
    elif operator == '*':
        return f'{num1 * num2}'
    elif operator == 'div':
        if num2 != 0:
            return f'{num1 / num2}'
        else:
            return 'Error: Division by zero'
    elif operator == '%':
        return f'{num1 % num2}'
    else:
        return 'Error: Invalid operator'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
