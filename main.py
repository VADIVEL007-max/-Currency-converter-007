from flask import Flask, render_template, request

app = Flask(__name__)

exchange_rates = {
    'USD': 1.0,
    'INR': 83.0,
    'EUR': 0.92,
    'GBP': 0.78,
    'JPY': 156.0
}

@app.route('/')
def home():
    return render_template("index.html", currencies=exchange_rates.keys())

@app.route('/convert', methods=['POST'])
def convert():
    from_curr = request.form['from_curr']
    to_curr = request.form['to_curr']
    amount = float(request.form['amount'])

    usd = amount / exchange_rates[from_curr]
    result = usd * exchange_rates[to_curr]

    return render_template("result.html", result=round(result, 2), to=to_curr)

if __name__ == '__main__':
    app.run(debug=True)
