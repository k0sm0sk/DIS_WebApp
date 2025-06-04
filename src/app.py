from flask import Flask, render_template, request, session, redirect, url_for
# We import render_template so we can render Jinja2 code, and request so we can handle POSTs
# We import sqlite, likely we don't need to install any new library because this is a default Python library
import sqlite3
import psycopg2
import re

# ? "\psql -h localhost -U postgres -d dis_projekt"


app = Flask(__name__)
app.secret_key = 'paklat'


@app.route('/', methods = ['GET','POST'])
def game_counter():


     # Check if user has entered their name
    if 'user_name' not in session:
        return redirect(url_for('enter_name'))
    
    if 'left_img' not in session:
        session['left_img'], session['left_name'],session['left_sales'] = random_game()

    if 'right_img' not in session:
        session['right_img'], session['right_name'], session['right_sales'] = random_game()
        
    if 'count' not in session:
        session['count'] = 0
    
    result = f"Score = {session['count']}"
    return render_template('game.html', 
                         result=result,
                         button1_text=session['left_name'],
                         button1_background=session['left_img'],
                         button2_text=session['right_name'],
                         button2_background=session['right_img'],
                         user_name=session['user_name'])

@app.route('/enter_name', methods=['GET', 'POST'])
def enter_name():
    if request.method == 'POST':
        name = request.form.get('name')
        pattern = r'^[A-Za-z]{3,15}$'  # Only letters, 3-15 characters long

        if name and re.match(pattern, name.strip()):
            session['user_name'] = name.strip()
            return redirect(url_for('game_counter'))
        else:
            return render_template('enter_name.html', error="Name must be 3–15 letters with no spaces or special characters.")
    
    return render_template('enter_name.html')


@app.route('/increment', methods=['POST'])
def increment():
    button = request.form.get('button')
    
    if 'count' not in session:
        session['count'] = 0

    if float(session['left_sales']) >= float(session['right_sales']) and button=='left':
        session['count'] += 1
        session['right_img'], session['right_name'], session['right_sales'] = random_game(float(session['right_sales']))
        
        
    if float(session['left_sales']) > float(session['right_sales']) and button=='right':
        app.logger.info(f"died")
        return new_game()
        
    if float(session['left_sales']) <= float(session['right_sales']) and button=='right':
        session['count'] += 1
        session['left_img'], session['left_name'],session['left_sales'] = random_game(float(session['right_sales']))
    
    if float(session['left_sales']) < float(session['right_sales']) and button=='left':
        app.logger.info(f"died")
        return new_game()
    
    return redirect(url_for('game_counter'))

@app.route('/random_game')
def random_game(cur_sales = 0.9):

    app.logger.info(f"cur_sales = {cur_sales}, type = {type(cur_sales)}")

    conn = sqlite3.connect('../data/game_data.db')

    cur = conn.cursor()
    
    cursor = conn.cursor()
    cur.execute(f"""
                SELECT img,title,total_sales FROM game_data 
                WHERE total_sales > {cur_sales} 
                ORDER BY RANDOM() 
                LIMIT 1;
                """)
    results = cursor.fetchall()

    rows = cur.fetchall()
    img = rows[0][0]
    name = rows[0][1]
    sales = rows[0][2]
    app.logger.info(f"name = {name}, sales = {sales}")
    return (f"https://www.vgchartz.com{img}", f"{name}", f"{sales}")

@app.route('/new_game', methods=['POST'])
def new_game():
    session['count'] = 0
    session['left_img'], session['left_name'],session['left_sales'] = random_game()
    session['right_img'], session['right_name'], session['right_sales'] = random_game()

    return redirect(url_for('game_counter'))
    
@app.route('/reset_name')
def reset_name():
    session.pop('user_name', None)
    return redirect(url_for('enter_name'))


if __name__ == '__main__':
    app.run(debug=True)
    
