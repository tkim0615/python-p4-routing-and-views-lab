#!/usr/bin/env python3
import ipdb
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:number>')
def count(number):
    count = ''
    for num in range(number):
        count += f'{num}\n'
    return count

# A math() view should take three parameters: num1, operation, and num2. It must perform the appropriate operation on
# the two numbers in the order that they are presented. The included operations 
# should be: +, -, *, div (/ would change the URL path), and %. Its URL should be of the format /math/<num1><operation><num2>.

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'operation not recognized'
    

    




if __name__ == '__main__':
    app.run(port=5555, debug=True)

# ipdb.set_trace()
