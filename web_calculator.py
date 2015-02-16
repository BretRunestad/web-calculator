from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def home_form():
    return render_template("calculator.html")

@app.route("/home", methods=["POST"])
def calculate():
    operand1 = float(request.form['operand1'])
    operator = request.select['operator']
    operand2 = float(request.form['operand2'])
    total = float()
    if operator == "+":
        total = operand1 + operand2
    elif operator == "-":
        total = operand1 - operand2
    elif operator == "*":
        total = operand1 * operand2
    elif operator == "/":
        total = operand1 / operand2

    return render_template("landing.html", result=total)

if __name__ == "__main__":
    app.run(debug=True)
