from flask import Flask, render_template, flash, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('gebruiker-request.html')
@app.route('/gebruiker.py', methods=['POST'])

def gebruiker():
    result = request.form
    return render_template('./gebruiker-response.html', result=result)

if __name__ == '__main__':
    app.run()