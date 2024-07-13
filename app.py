from flask import Flask, render_template, request, redirect, url_for
from model import quote_return
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote', methods=['POST'])
def quote():
    try:
        feeling = request.form['feeling']
        return render_template('quote.html', feeling=quote_return(feeling))
    except KeyError:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
