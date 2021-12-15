from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    history = []
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        if not request.form['value1'].isnumeric() or not request.form['value2'].isnumeric():
            error = 'Incorrect Inputs. Please Try Again.'
        else:
            flash('You successfully calculated')
            flash('You are awesome')

            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            CalculatorController.history.append(result)
            data = CalculatorController.history
            return render_template('result.html', data=data, value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator2.html', error=error)

    @staticmethod
    def get():
        """returns calculator page"""
        return render_template('calculator2.html')

    @staticmethod
    def AAA():
        """returns aaa page"""
        return render_template('AAA.html')

    @staticmethod
    def azure():
        """returns python page"""
        return render_template('azure.html')

    @staticmethod
    def OOP():
        """returns soc page"""
        return render_template('OOP.html')

    @staticmethod
    def concepts():
        """returns oop page"""
        return render_template('concepts.html')
