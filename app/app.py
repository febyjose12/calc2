"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()
@app.route("/AAA", methods=['GET'])
def AAA_get():

    return CalculatorController.AAA()

@app.route("/azure", methods=['GET'])
def azure_get():

    return CalculatorController.azure()

@app.route("/concepts", methods=['GET'])
def concepts_get():
    """get concepts page"""
    return CalculatorController.concepts()

@app.route("/OOP", methods=['GET'])
def oop_get():
    """get OOP page"""
    return CalculatorController.OOP()