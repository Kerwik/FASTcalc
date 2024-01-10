from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Получаем данные из формы
    number1 = request.form.get('number1', type=float)
    number2 = request.form.get('number2', type=float)
    operation = request.form.get('operation')

    if operation == 'add':
        result = number1 + number2
    elif operation == 'subtract':
        result = number1 - number2
    elif operation == 'multiply':
        result = number1 * number2
    elif operation == 'divide':
        result = number1 / number2
    else:
        result = 'Invalid operation'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)