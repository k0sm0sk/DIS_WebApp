from flask import Flask, render_template, request, session, redirect, url_for
# We import render_template so we can render Jinja2 code, and request so we can handle POSTs
# We import sqlite, likely we don't need to install any new library because this is a default Python library

app = Flask(__name__)
app.secret_key = 'paklat'

@app.route('/', methods=['GET', 'POST'])

def game_counter():
    if 'count' not in session:
        session['count'] = 0
    
    if request.method == 'POST':
        session['count'] += 1
        return redirect(url_for('game_counter'))
    
    result = f"Score = {session['count']}"
    return render_template('game.html', result=result)


@app.route('/test', methods=['GET', 'POST'])
def func_runner():
    return tester(), testing()

def tester():
    return "test"

def testing():
    return "hallo"

if __name__ == '__main__':
    app.run(debug=True)
    

@app.route('/vitus', methods = ['GET','POST'])
def vitus():
    return "execute order 66"
    
